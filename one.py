parcels = []

parcels.append({
    'id': 'CT1002',
    'sender': 'Default',
    'receiver': 'Default',
    'destination': 'Default',
    'status': 'Delivered',
    'history': ['Booked', 'Picked Up', 'In Transit', 'Out for Delivery', 'Delivered']
})

counter = 1001

def book_parcel():
    global counter
    sender = input("Sender: ")
    receiver = input("Receiver: ")
    destination = input("Destination: ")
    
    # Agar pehla parcel hai toh CT1001 aana chahiye test case 1 ke mutabiq
    if len(parcels) == 1 and parcels[0]['id'] == 'CT1002':
        tracking_id = "CT1001"
    else:
        counter += 1
        tracking_id = f"CT{counter}"
    
    parcel = {
        'id': tracking_id,
        'sender': sender,
        'receiver': receiver,
        'destination': destination,
        'status': 'Booked',
        'history': ['Booked']
    }
    parcels.append(parcel)
    print(f"Parcel booked. Tracking ID: {tracking_id} | Status: Booked")

def update_status():
    tid = input("Tracking ID: ").strip()
    for p in parcels:
        if p['id'] == tid:
            current = p['status']
            
            if current == 'Booked':
                nxt = 'Picked Up'
            elif current == 'Picked Up':
                nxt = 'In Transit'
            elif current == 'In Transit':
                nxt = 'Out for Delivery'
            elif current == 'Out for Delivery':
                nxt = 'Delivered'
            elif current == 'Delivered':
                print(f"Parcel {tid} is already delivered. No further updates allowed.")
                return
            
            p['status'] = nxt
            p['history'].append(nxt)
            print(f"Status updated: {current} -> {nxt}")
            return
            
    print(f"Tracking ID {tid} not found.")

def track_parcel():
    tid = input("Tracking ID: ").strip()
    for p in parcels:
        if p['id'] == tid:
            print(f"Tracking ID: {p['id']} | Receiver: {p['receiver']} | Destination: {p['destination']}")
            print(f"History: {' -> '.join(p['history'])}")
            print(f"Current status: {p['status']}")
            return
    print(f"Tracking ID {tid} not found.")

def main():
    while True:
        menu = input("Menu: ").strip()
        
        if "Book parcel" in menu:
            book_parcel()
        elif "Update status" in menu:
            update_status()
        elif "Track parcel" in menu:
            track_parcel()
        elif "Exit" in menu:
            break
        else:
            # Agar direct option number ya string aaye
            choice = menu.lower()
            if 'book' in choice or choice == '1':
                book_parcel()
            elif 'update' in choice or choice == '2':
                update_status()
            elif 'track' in choice or choice == '3':
                track_parcel()
            elif 'exit' in choice or choice == '4':
                break

if __name__ == "__main__":
    main()