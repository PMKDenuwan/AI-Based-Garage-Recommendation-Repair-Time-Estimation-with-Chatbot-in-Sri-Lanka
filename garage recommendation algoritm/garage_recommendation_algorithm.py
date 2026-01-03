import os

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    """Print styled header"""
    print("\n" + "="*70)
    print(f" {text}")
    print("="*70)

def print_subheader(text):
    """Print styled subheader"""
    print(f"\n{'─'*70}")
    print(f" {text}")
    print(f"{'─'*70}")

def get_garage_details(garage_num):
    """Get details for a single garage using array format"""
    print(f"\n🏚️  GARAGE {garage_num:02d}")
    print("─" * 70)
    print('  Format: ["Name", Distance(km), Waiting(min), Arrival(min), Rating, Mechanics]')
    print('  Example: ["Garage 01", 0.50, 15, 2, 3.2, 2]')
    print("─" * 70)
    
    while True:
        try:
            user_input = input(f"\n  Enter data: ")
            # Parse the input as a Python list
            data = eval(user_input)
            
            if not isinstance(data, list) or len(data) != 6:
                print("  ❌ Error: Please enter exactly 6 values in the format shown above.")
                continue
            
            return {
                'name': str(data[0]),
                'distance': float(data[1]),
                'waiting': float(data[2]),
                'arrival': float(data[3]),
                'rating': float(data[4]),
                'mechanics': int(data[5])
            }
        except Exception as e:
            print(f"  ❌ Error: Invalid format. Please try again.")
            print(f"  {str(e)}")

def display_input_summary(garages):
    """Display all entered garage data in a table"""
    print_header("📋 GARAGE DETAILS SUMMARY (YOUR INPUTS)")
    
    print(f"\n{'Garage Name':<20}{'Distance':<12}{'Waiting':<14}{'Arrival':<14}{'Rating':<10}{'Mechanics':<10}")
    print(f"{'':20}{'(km)':<12}{'(min)':<14}{'(min)':<14}{'(★)':<10}{'':10}")
    print("─" * 80)
    
    for garage in garages:
        print(f"{garage['name']:<20}{garage['distance']:<12.2f}{garage['waiting']:<14.0f}"
              f"{garage['arrival']:<14.0f}{garage['rating']:<10.1f}{garage['mechanics']:<10}")
    
    print("─" * 80)
    print(f"\n  Total Garages Entered: {len(garages)}")
    print("─" * 80)

def normalize_values(garages):
    """Normalize all values and calculate scores"""
    print_header("📊 STEP 1: FIND MAXIMUM VALUES")
    
    max_distance = max(g['distance'] for g in garages)
    max_waiting = max(g['waiting'] for g in garages)
    max_arrival = max(g['arrival'] for g in garages)
    max_mechanics = max(g['mechanics'] for g in garages)
    
    print(f"\n  Max Distance  = {max_distance:.2f} km")
    print(f"  Max Waiting   = {max_waiting:.2f} min")
    print(f"  Max Arrival   = {max_arrival:.2f} min")
    print(f"  Max Mechanics = {max_mechanics}")
    
    return max_distance, max_waiting, max_arrival, max_mechanics

def calculate_scores(garages, max_distance, max_waiting, max_arrival, max_mechanics):
    """Calculate normalized scores for all garages"""
    
    # Weights
    W_DISTANCE = 0.25
    W_WAITING = 0.30
    W_ARRIVAL = 0.15
    W_RATING = 0.20
    W_MECHANICS = 0.10
    
    print_header("⚖️  STEP 2: WEIGHTS (FIXED)")
    print(f"\n  Distance Weight  = {W_DISTANCE}")
    print(f"  Waiting Weight   = {W_WAITING}")
    print(f"  Arrival Weight   = {W_ARRIVAL}")
    print(f"  Rating Weight    = {W_RATING}")
    print(f"  Mechanics Weight = {W_MECHANICS}")
    
    print_header("🧮 STEP 3: NORMALIZATION FORMULAS")
    print("\n  distanceNorm  = distance / maxDistance")
    print("  waitingNorm   = waiting / maxWaiting")
    print("  arrivalNorm   = arrival / maxArrival")
    print("  ratingNorm    = (5 - rating) / 5")
    print("  mechanicsNorm = (maxMechanics - mechanics) / maxMechanics")
    
    print_header("🧮 STEP 4: CALCULATE SCORES FOR EACH GARAGE")
    
    results = []
    
    for i, garage in enumerate(garages, 1):
        print(f"\n{'─'*70}")
        print(f"🏚️  {garage['name'].upper()}")
        print(f"{'─'*70}")
        
        # Normalize values
        dist_norm = garage['distance'] / max_distance if max_distance > 0 else 0
        wait_norm = garage['waiting'] / max_waiting if max_waiting > 0 else 0
        arrival_norm = garage['arrival'] / max_arrival if max_arrival > 0 else 0
        rating_norm = (5 - garage['rating']) / 5
        mechanic_norm = (max_mechanics - garage['mechanics']) / max_mechanics if max_mechanics > 0 else 0
        
        print(f"\n  Normalized Values:")
        print(f"  ├─ Distance:  {garage['distance']:.2f} / {max_distance:.2f} = {dist_norm:.4f}")
        print(f"  ├─ Waiting:   {garage['waiting']:.2f} / {max_waiting:.2f} = {wait_norm:.4f}")
        print(f"  ├─ Arrival:   {garage['arrival']:.2f} / {max_arrival:.2f} = {arrival_norm:.4f}")
        print(f"  ├─ Rating:    (5 - {garage['rating']:.1f}) / 5 = {rating_norm:.4f}")
        print(f"  └─ Mechanics: ({max_mechanics} - {garage['mechanics']}) / {max_mechanics} = {mechanic_norm:.4f}")
        
        # Calculate final score
        final_score = (
            dist_norm * W_DISTANCE +
            wait_norm * W_WAITING +
            arrival_norm * W_ARRIVAL +
            rating_norm * W_RATING +
            mechanic_norm * W_MECHANICS
        )
        
        print(f"\n  Final Score Calculation:")
        print(f"  ({dist_norm:.4f} × {W_DISTANCE}) + ({wait_norm:.4f} × {W_WAITING}) + "
              f"({arrival_norm:.4f} × {W_ARRIVAL}) + ({rating_norm:.4f} × {W_RATING}) + "
              f"({mechanic_norm:.4f} × {W_MECHANICS})")
        print(f"\n  = {dist_norm * W_DISTANCE:.4f} + {wait_norm * W_WAITING:.4f} + "
              f"{arrival_norm * W_ARRIVAL:.4f} + {rating_norm * W_RATING:.4f} + "
              f"{mechanic_norm * W_MECHANICS:.4f}")
        print(f"\n  ✅ FINAL SCORE = {final_score:.4f}")
        
        results.append({
            'garage': garage,
            'score': final_score
        })
    
    return results

def display_ranking(results):
    """Display final ranking"""
    print_header("🏆 FINAL RANKING (LOWEST SCORE = BEST)")
    
    # Sort by score (lowest is best)
    sorted_results = sorted(results, key=lambda x: x['score'])
    
    medals = ['🥇', '🥈', '🥉']
    
    print(f"\n{'Rank':<8}{'Garage':<25}{'Distance':<12}{'Waiting':<12}{'Rating':<10}{'Score':<10}")
    print("─" * 77)
    
    for i, result in enumerate(sorted_results, 1):
        garage = result['garage']
        score = result['score']
        
        medal = medals[i-1] if i <= 3 else f" {i}  "
        
        print(f"{medal:<8}{garage['name']:<25}{garage['distance']:.2f} km{'':<5}"
              f"{garage['waiting']:.0f} min{'':<6}{garage['rating']:.1f}{'':<6}{score:.4f}")
    
    print("\n" + "─" * 77)
    print(f"\n✅ BEST RECOMMENDATION: {sorted_results[0]['garage']['name']} "
          f"(Score: {sorted_results[0]['score']:.4f})")
    print("─" * 77)

def main():
    clear_screen()
    
    print("="*70)
    print(" 🚗 GARAGE RECOMMENDATION ALGORITHM")
    print(" 📍 Driver Location: SLIIT, New Kandy Road, Malabe (6.914833, 79.972861)")
    print("="*70)
    
    # Get number of garages
    radius = 2.5
    num_garages = int(input(f"\n❓ How many garages discovered within {radius}km radius? "))
    
    # Collect garage details
    garages = []
    print_subheader("📝 ENTER GARAGE DETAILS")
    
    for i in range(num_garages):
        garage = get_garage_details(i + 1)
        garages.append(garage)
    
    # Display summary of all inputs
    display_input_summary(garages)
    
    # Wait for user to review
    input("\n⏸️  Press ENTER to continue with calculations...")
    
    # Normalize and calculate
    max_distance, max_waiting, max_arrival, max_mechanics = normalize_values(garages)
    
    # Calculate scores
    results = calculate_scores(garages, max_distance, max_waiting, max_arrival, max_mechanics)
    
    # Display ranking
    display_ranking(results)
    
    print("\n🎉 Analysis Complete!\n")

if __name__ == "__main__":
    main()