from dataclasses import dataclass

@dataclass
class Request:
    user_id: int | None
    permissions: list[str]
    data: dict

def process_request(request: Request):
    print(f"--- Processing request for user {request.user_id} ---")
    
    # 1. Authentication Check
    if request.user_id is None:
        print("HANDLER: Authentication failed. Request rejected.")
        return # Stop processing
    else:
        print("HANDLER: Authentication successful.")
        
        # 2. Authorization Check (nested logic)
        if "admin" not in request.permissions:
            print("HANDLER: Authorization failed. User is not an admin. Request rejected.")
            return # Stop processing
        else:
            print("HANDLER: Authorization successful.")
            
            # 3. Caching Check (more nested logic)
            if request.data.get("use_cache", False):
                print("HANDLER: Cache hit. Returning cached data.")
                return # Stop processing
            else:
                print("HANDLER: Cache miss. Processing request...")
                # The final business logic would go here
                print("Final processing complete.")


# Client Code
req1 = Request(user_id=None, permissions=[], data={}) # Fails auth
process_request(req1)

print("\n" + "="*20 + "\n")

req2 = Request(user_id=101, permissions=["read"], data={}) # Fails authorization
process_request(req2)

print("\n" + "="*20 + "\n")

req3 = Request(user_id=7, permissions=["read", "admin"], data={}) # Passes all checks
process_request(req3)