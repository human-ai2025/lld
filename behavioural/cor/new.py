from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class Request:
    user_id: int | None
    permissions: list[str]
    data: dict

# --- The Handler Interface (or Abstract Base Class) ---
class Handler(ABC):
    def __init__(self, next_handler: Optional['Handler'] = None):
        self._next_handler = next_handler

    # A fluent interface for chaining
    def set_next(self, handler: 'Handler') -> 'Handler':
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Request) -> Optional[str]:
        # The core logic: if there's a next handler, pass it on.
        # DRY
        if self._next_handler:
            return self._next_handler.handle(request)
        # End of the chain
        return None

# --- Concrete Handlers ---
class AuthenticationHandler(Handler):
    def handle(self, request: Request) -> Optional[str]:
        print("-> Checking Authentication...")
        if request.user_id is None:
            return "Authentication Failed: No user is logged in."
        # If successful, pass to the next handler
        return super().handle(request)

class AuthorizationHandler(Handler):
    def handle(self, request: Request) -> Optional[str]:
        print("-> Checking Authorization...")
        if "admin" not in request.permissions:
            return "Authorization Failed: User lacks admin permissions."
        return super().handle(request)

class CacheHandler(Handler):
    def handle(self, request: Request) -> Optional[str]:
        print("-> Checking Cache...")
        if request.data.get("use_cache", False):
            return "Success: Returning response from cache."
        return super().handle(request)

# --- The Client ---
def client_code(handler: Handler, request: Request):
    result = handler.handle(request)
    if result:
        print(f"\nFinal Result: {result}")
    else:
        # This means the request passed all checks in the chain
        print("\nFinal Result: All checks passed. Executing final business logic.")

# Build the chain of responsibility
# auth -> authz -> cache
auth_handler = AuthenticationHandler()
auth_handler.set_next(AuthorizationHandler()).set_next(CacheHandler())

print("--- Scenario 1: Fails Authentication ---")
req1 = Request(user_id=None, permissions=[], data={})
client_code(auth_handler, req1)

print("\n" + "="*40 + "\n")

print("--- Scenario 2: Fails Authorization ---")
req2 = Request(user_id=101, permissions=["read"], data={})
client_code(auth_handler, req2)

print("\n" + "="*40 + "\n")

print("--- Scenario 3: Passes all checks ---")
req3 = Request(user_id=7, permissions=["read", "admin"], data={})
client_code(auth_handler, req3)