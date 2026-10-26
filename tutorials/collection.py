## LIST 


collection = ["omafu", "jireh","victor","eboh", 1,2,3,4,True,False]

# print(collection)

# boyjireh = collection.pop(1)

# print(collection)
# print(boyjireh)

# collection.insert(3, "jireh")

# print(collection)


# for item in collection:

#     print(item)

# for num in range(len(collection)):

#     print(num)


# def Guest_Manager():
#     """Manages the guest registration, VIP additions, and security removals."""

#     guest_list = []
#     for i in range(1, 4):

#         name = input(f"Guest {i} Enter your Name: ")
#         guest_list.append(name)

#     guest_list.insert(0, "VIP_Sherlock")
#     guest_list.append("Unwanted_Guest")
#     print(guest_list)

#     guest_list.remove("Unwanted_Guest")

#     removed_guest = guest_list.pop()

#     print(f"Sorry, {removed_guest}, the venue is full.")

#     print(guest_list)

# def main():

#     Guest_Manager()

# if __name__ == "__main__":
#     main()

import threading  # Built-in thread protection
from typing import List, Dict, Any

# ==========================================
# 1. CUSTOM SYSTEM EXCEPTIONS
# ==========================================

class SecurityException(Exception):
    """Raised when a blacklisted entity attempts an action."""
    pass

class CapacityException(Exception):
    """Raised when the infrastructure threshold is exceeded."""
    pass

# ==========================================
# 2. DATA LAYER (Replaces Pydantic with Native Properties)
# ==========================================

class Guest:
    """Validates and holds guest data using native Python descriptors."""
    def __init__(self, name: str, vip_status: bool = False):
        self.name = name  # This triggers the setter validation automatically
        self.vip_status = vip_status

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Native runtime validation logic."""
        if not isinstance(value, str):
            raise TypeError("Name field must be a string text string.")
        
        cleaned = value.strip().title()
        if len(cleaned) < 2 or len(cleaned) > 50:
            raise ValueError("Name length must be between 2 and 50 characters.")
        if not cleaned.replace(" ", "").isalpha():
            raise ValueError("Name must contain alphabetic characters only.")
        
        self._name = cleaned

    def to_dict(self) -> Dict[str, Any]:
        """Serializes the data structure natively."""
        return {"name": self._name, "vip_status": self.vip_status}


# ==========================================
# 3. CORE CORE MANAGER (Thread-Safe OOP)
# ==========================================

class RobustGuestManager:
    def __init__(self, capacity: int, blacklist: List[str]):
        self._guest_pool: List[Guest] = []  # Strictly encapsulated data list
        self.capacity = capacity
        self.blacklist = [name.strip().title() for name in blacklist]
        self._lock = threading.Lock()  # System thread lock for memory safety

    def register_guest(self, guest: Guest) -> None:
        """Appends a validated guest to the pool safely under lock."""
        with self._lock:
            if guest.name in self.blacklist:
                raise SecurityException(f"🚫 ACCESS DENIED: {guest.name} is on the security blacklist.")
            
            if len(self._guest_pool) >= self.capacity:
                raise CapacityException(f"❌ REGISTRATION FAILURE: Venue capacity of {self.capacity} reached.")
            
            self._guest_pool.append(guest)
            print(f"✅ Successfully Registered: {guest.name} (VIP: {guest.vip_status})")

    def prioritize_vip(self, vip_guest: Guest) -> None:
        """Inserts a high-priority entity safely at index 0."""
        with self._lock:
            vip_guest.vip_status = True
            self._guest_pool.insert(0, vip_guest)
            print(f"⭐ VIP Injected into Pipeline: {vip_guest.name}")

    def evict_guest(self, name: str) -> None:
        """Gracefully removes a target item. Handles value anomalies."""
        with self._lock:
            formatted_name = name.strip().title()
            # Linear scan abstraction over structural mutation
            matching_guests = [g for g in self._guest_pool if g.name == formatted_name]
            
            if not matching_guests:
                print(f"ℹ️ Eviction Idle: '{formatted_name}' was not present in the system matrix.")
                return

            for guest in matching_guests:
                self._guest_pool.remove(guest)
                print(f"🔥 Evicted: {guest.name} has been forcefully expunged.")

    def enforce_capacity_cutoff(self) -> Guest:
        """Pops the tail-end item safely, conforming to system restrictions."""
        with self._lock:
            if not self._guest_pool:
                raise IndexError("Pipeline underflow: Cannot pop from an empty guest pool.")
            
            evicted_individual = self._guest_pool.pop()
            print(f"⚠️ Capacity Cutoff: {evicted_individual.name} was popped from the stack allocation.")
            return evicted_individual

    def snapshot_registry(self) -> List[Dict[str, Any]]:
        """Exposes raw read-only dictionary representations of state data."""
        return [guest.to_dict() for guest in self._guest_pool]


# ==========================================
# 4. ORCHESTRATION PIPELINE
# ==========================================

def simulate_registration(manager: RobustGuestManager, raw_name: str):
    """Simulates a registration system processing hit with localized catch blocks."""
    try:
        # Business logic instantiation
        guest_payload = Guest(name=raw_name)
        manager.register_guest(guest_payload)
    except (ValueError, TypeError, SecurityException, CapacityException) as err:
        print(f"Context Handled Exception -> {err}")


def main():
    # Instantiate the system engine entirely out-of-the-box
    manager = RobustGuestManager(capacity=3, blacklist=["Unwanted_Guest", "Malicious_Actor"])

    print("=== Phase 1: High Ingestion Traffic Validation ===")
    simulate_registration(manager, "Alice Smith")
    simulate_registration(manager, "Unwanted_Guest")  # SecurityException
    simulate_registration(manager, "Bob Jones")
    simulate_registration(manager, "Charlie 123")    # ValueError (numbers checked natively)
    simulate_registration(manager, "David Miller")
    simulate_registration(manager, "Eve Adams")       # CapacityException

    print("\n=== Phase 2: System Mutators ===")
    manager.prioritize_vip(Guest(name="Sherlock Holmes"))
    manager.evict_guest("Unwanted_Guest")  
    manager.enforce_capacity_cutoff()

    print("\n=== Phase 3: Final State Registry Snapshot ===")
    print(manager.snapshot_registry())


if __name__ == "__main__":
    main()


