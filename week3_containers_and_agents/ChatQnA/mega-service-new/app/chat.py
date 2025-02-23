from comps import ServiceOrchestrator
from comps import MicroService, ServiceRoleType
from comps.cores.proto.api_protocol import ChatCompletionRequest, ChatCompletionResponse
from fastapi import Request

# Common server connectivity issues to check:
# 1. Port 8888 may be blocked by firewall or already in use
# 2. Host 0.0.0.0 allows connections from any IP - make sure this is intended
# 3. No error handling around server startup
# 4. No logging to debug connection issues
# 5. handle_request() doesn't return any response

class Chat:
    def __init__(self):
        print("init") # Consider using proper logging instead of print
        self.megaservice = ServiceOrchestrator()
        self.endpoint = "/chat"
        self.host = "0.0.0.0" # Consider localhost (127.0.0.1) for local testing
        self.port = 8888 # Verify this port is available

    def add_remote_services(self):
        print("add_remote_services")
        
    def start(self):
        print("start")
        # This microservice Megaservice becomes the main entrypoint fo the app 
        self.service = MicroService(
            self.__class__.__name__,
            service_role=ServiceRoleType.MEGASERVICE,
            host=self.host,
            port=self.port,
            endpoint=self.endpoint,
            input_datatype=ChatCompletionRequest,
            output_datatype=ChatCompletionResponse,
        )

        self.service.add_route(self.endpoint, self.handle_request, methods=["POST"])

        self.service.start()

    def handle_request(self, request: Request):
        print("handle_request") # Should return a response
    
if __name__ == "__main__":
    print("main")
    chat = Chat()
    chat.add_remote_services()
    chat.start()
