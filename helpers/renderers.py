import json
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList

message_map = lambda view: lambda status_code: {  # noqa
    "POST": "%s created successfully" % view.name.capitalize(),
    "PATCH": "%s updated succesfully" % view.name.capitalize(),
    "DELETE": "%s deleted successfully" % view.name.capitalize(),
}.get(status_code)



class UserJSONRenderer(JSONRenderer):
    """
    Renderer which serializes data to JSON.
    """

    charset = "utf-8"

    def render(
        self,
        data: Union[
            Dict[str, ErrorDetail],
            ReturnDict,
            Dict[str, Union[str, List[ErrorDetail]]],
            Dict[str, Union[str, Dict[str, str]]],
            Dict[str, str],
        ],
        media_type: Optional[str] = None,
        renderer_context: Optional[Dict[str, Any]] = None,
    ) -> Union[str, bytes]:
        # If the view throws an error (such as the user can't be authenticated
        # or something similar), `data` will contain an `errors` key. We want
        # the default JSONRenderer to handle rendering errors, so we need to
        # check for this case.
        if renderer_context["response"].status_code == 422:
            renderer_context[
                "response"
            ].status_code = status.HTTP_400_BAD_REQUEST
        status_code = renderer_context["response"].status_code

        return (
            json.dumps(data)
            if status.is_success(status_code)
            else super(UserJSONRenderer, self).render(
                {
                    "message": data.pop("message", "Fix the error(s) below"),
                    "errors": data,
                }
            )
        )

class DefaultRenderer(JSONRenderer):
    """
    custom renderer class for application views
    """

    def render(
        self,
        data: Union[Dict[str, Union[str, List[ErrorDetail]]], ReturnList],
        accepted_media_type: Optional[str] = None,
        renderer_context: Optional[Dict[str, Any]] = None,
    ) -> bytes:
        """
        format response data for application views
        """
        if renderer_context["response"].status_code == 422:
            renderer_context[
                "response"
            ].status_code = status.HTTP_400_BAD_REQUEST
        status_code = renderer_context["response"].status_code
        if renderer_context["request"].method == "GET":
            if renderer_context["kwargs"] == {}:
                message = (
                    "All %s" 
                    % renderer_context["view"].pluralized_name.capitalize()
                )
            else:
                message = (
                    "%s info" % renderer_context["view"].name.capitalize()
                )
        else:
            message = message_map(renderer_context["view"])(
                renderer_context["request"].method
            )
        data = (
            ({"status": "success", "message": message, "data": data})
            if status.is_success(status_code)
            else {
                "status": "error",
                "message": "Correct the errors below",
                "data": data,
            }
        )
        return super(DefaultRenderer, self).render(
            data, accepted_media_type, renderer_context
        )
