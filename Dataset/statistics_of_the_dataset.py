import pandas as pd
import numpy as np
import random

# ==========================================
# 1. GENERATION LOGIC (As approved previously)
# ==========================================
# Strict Location Lists
LOC_COLOMBO_SPECIFIC = [
    'Borella', 'Kollupitiya', 'Bambalapitiya', 'Havelock Town', 'Kirulapone', 
    'Grandpass', 'Slave Island', 'Modara', 'Maradana'
]
LOC_COLOMBO_OTHER = [
    'Kaduwela', 'Kesbewa', 'Kolonnawa', 'Dehiwala', 'Seethawaka', 'Ratmalana', 'Padukka'
]

LOC_MATARA_SPECIFIC = [
    'Matara', 'Meddawatta', 'Walgama', 'Nupe', 'Dondra', 'Weligama', 'Nawimana', 
    'Thihagoda', 'Pallimulla', 'Paburana', 'Dikwella', 'Gandara', 'Thalalla', 
    'Hiththetiya', 'Akuressa'
]
LOC_MATARA_OTHER = [
    'Athuraliya', 'Devinuwara', 'Hakmana', 'Kamburupitiya', 'Kirinda Puhulwella', 
    'Kotapola', 'Malimbada', 'Mulatiyana', 'Pasgoda', 'Pitabeddara', 'Welipitiya'
]

COUNTS = {
    'Colombo_Specific': 97,    
    'Colombo_Other': 132,      
    'Matara_Specific': 343,    
    'Matara_Other': 303        
}

GARAGE_TYPES = ['Authorized', 'Local']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
TIMES = ['Morning', 'Afternoon', 'Evening']

FAULT_DB = {
    'Engine': [
        ('Oil Leak (Gasket)',       [0.4, 0.5, 0.1], 2.5,  'Valve Cover Gasket'),
        ('Misfiring',               [0.3, 0.5, 0.2], 1.5,  'Spark Plugs/Coils'),
        ('Timing Belt Noise',       [0.2, 0.6, 0.2], 3.5,  'Timing Belt Kit'),
        ('Engine Knocking',         [0.0, 0.2, 0.8], 15.0, 'Engine Overhaul Kit'),
        ('Hard Starting',           [0.5, 0.4, 0.1], 1.0,  'Starter Motor/Battery'),
        ('Coolant Leak',            [0.4, 0.4, 0.2], 1.5,  'Radiator Hose/Pipe'),
        ('Throttle Body Issue',     [0.6, 0.3, 0.1], 1.0,  'Throttle Body Cleaner'),
        ('Fuel Injector Clog',      [0.3, 0.6, 0.1], 2.0,  'Injector Cleaning'),
        ('Radiator Fan Failure',    [0.2, 0.7, 0.1], 3.0,  'Fan Motor'),
        ('Thermostat Stuck',        [0.3, 0.6, 0.1], 3.0,  'Thermostat Valve'),
        ('Water Pump Failure',      [0.1, 0.5, 0.4], 4.0,  'Water Pump'),
        ('Blown Head Gasket',       [0.0, 0.1, 0.9], 15.0, 'Head Gasket Set'), 
        ('Radiator Cap Fault',      [0.9, 0.1, 0.0], 0.5,  'Radiator Cap'),    
    ],
    'Electrical': [
        ('Battery Drain',           [0.8, 0.2, 0.0], 0.5,  'Battery'),
        ('Alternator Failure',      [0.1, 0.4, 0.5], 2.5,  'Alternator'),
        ('Starter Motor Fault',     [0.2, 0.5, 0.3], 2.0,  'Starter Motor'),
        ('Power Window Stuck',      [0.5, 0.4, 0.1], 1.5,  'Window Motor/Regulator'),
        ('Headlight Issue',         [0.8, 0.2, 0.0], 0.5,  'Bulb/Fuse'),
        ('Horn Not Working',        [0.9, 0.1, 0.0], 0.5,  'Horn Unit'),
        ('Check Engine Light',      [0.5, 0.4, 0.1], 1.0,  'Sensor (O2/MAP)'),
        ('Rat Bite Damage',         [0.3, 0.5, 0.2], 3.0,  'Wiring Harness Repair'), 
    ],
    'Suspension': [
        ('Shock Absorber Leaking',  [0.2, 0.7, 0.1], 2.0,  'Shock Absorbers'),
        ('Bushings Worn',           [0.3, 0.6, 0.1], 3.0,  'Suspension Bush Kit'),
        ('Wheel Bearing Noise',     [0.1, 0.6, 0.3], 2.5,  'Wheel Bearing'),
        ('CV Joint Noise',          [0.1, 0.5, 0.4], 2.5,  'CV Joint/Boot'),
        ('Steering Rack Rattle',    [0.1, 0.5, 0.4], 4.0,  'Steering Rack Bush'),
        ('Rim Bend',                [0.6, 0.3, 0.1], 1.0,  'Rim Repair'), 
    ],
    'Brake': [
        ('Brake Pad Wear',          [0.7, 0.3, 0.0], 1.0,  'Brake Pads'),
        ('Brake Shoe Wear',         [0.6, 0.4, 0.0], 1.5,  'Brake Shoes'),
        ('ABS Sensor Fault',        [0.4, 0.5, 0.1], 1.0,  'ABS Sensor'),
        ('Brake Fluid Leak',        [0.2, 0.5, 0.3], 2.0,  'Brake Cylinder/Line'),
        ('Disc Rotor Warped',       [0.1, 0.6, 0.3], 1.5,  'Disc Skimming'),
    ],
    'Transmission': [
        ('Clutch Slipping',         [0.0, 0.3, 0.7], 5.0,  'Clutch Plate Set'),
        ('Gear Shifting Hard',      [0.2, 0.5, 0.3], 3.0,  'Gear Cable/Oil'),
        ('Transmission Oil Leak',   [0.3, 0.5, 0.2], 2.0,  'Oil Seal'),
        ('CVT Jerking (AGS)',       [0.1, 0.4, 0.5], 4.0,  'AGS Actuator/Oil'),
    ],
    'AC': [
        ('No Cooling',              [0.3, 0.4, 0.3], 2.0,  'Refrigerant Gas'),
        ('Compressor Noise',        [0.1, 0.3, 0.6], 3.5,  'Compressor'),
        ('Blower Fan Issue',        [0.5, 0.4, 0.1], 1.0,  'Blower Motor'),
        ('Condenser Leak',          [0.2, 0.5, 0.3], 2.5,  'Condenser'),
        ('Bad Smell',               [0.8, 0.2, 0.0], 1.0,  'Evaporator Cleaning'), 
    ],
    'Body': [
        ('Bumper Crack',            [0.8, 0.2, 0.0], 2.0,  'Bumper Repair'),
        ('Door Rattle',             [0.7, 0.3, 0.0], 1.0,  'Door Panel Clips'),
        ('Paint Scratch',           [0.9, 0.1, 0.0], 2.0,  'Touch-up Paint'),
        ('Windshield Crack',        [0.1, 0.6, 0.3], 3.0,  'Windshield Glass'),
        ('Rust Patch',              [0.5, 0.4, 0.1], 5.0,  'Tinkering/Painting'), 
    ]
}

CAT_WEIGHTS = {
    'Engine': 0.28, 'Electrical': 0.18, 'Brake': 0.16, 
    'Suspension': 0.14, 'AC': 0.14, 'Transmission': 0.06, 'Body': 0.04
}

def generate_rows(num_rows, location_list):
    batch_data = []
    for _ in range(num_rows):
        location = random.choice(location_list)
        model_year = random.randint(2011, 2022)
        age = 2024 - model_year
        usage = np.random.choice(['Taxi', 'Normal', 'Low'], p=[0.2, 0.6, 0.2])
        if usage == 'Taxi': mileage = int(age * random.randint(25000, 45000) * random.uniform(0.9, 1.1))
        elif usage == 'Low': mileage = int(age * random.randint(3000, 8000) * random.uniform(0.8, 1.2))
        else: mileage = int(age * random.randint(10000, 18000) * random.uniform(0.8, 1.2))
        mileage = max(mileage, 5000)
        
        if age <= 3: garage_prob = [0.8, 0.2]
        elif age <= 7: garage_prob = [0.4, 0.6]
        else: garage_prob = [0.15, 0.85]
        garage_type = np.random.choice(GARAGE_TYPES, p=garage_prob)
        expertise = random.randint(5, 20) if garage_type == 'Authorized' else random.randint(1, 25)
        
        cat = np.random.choice(list(CAT_WEIGHTS.keys()), p=list(CAT_WEIGHTS.values()))
        fault = random.choice(FAULT_DB[cat])
        f_type, f_probs, base_time, part = fault
        severity = np.random.choice(['Minor', 'Moderate', 'Major'], p=f_probs)
        
        sev_mult = {'Minor': 0.5, 'Moderate': 1.0, 'Major': 2.5}
        exp_factor = 1.5 - ((expertise - 1) * (0.8 / 24))
        noise = random.uniform(0.85, 1.3)
        hours = round(max(0.5, base_time * sev_mult[severity] * exp_factor * noise), 1)
        
        if random.random() < 0.015:
            hours = 0.0
            
        avail_prob = [0.4, 0.6] if (age > 10 and severity == 'Major') else [0.85, 0.15]
        parts_avail = np.random.choice(['In Stock', 'Order Required'], p=avail_prob)
        
        batch_data.append({
            'Car_Model': 'Suzuki Alto',
            'Model_Year': model_year,
            'Mileage_KM': mileage,
            'Fault_Category': cat,
            'Fault_Type': f_type,
            'Severity': severity,
            'Parts_Required': part,
            'Parts_Availability': parts_avail,
            'Garage_Type': garage_type,
            'Mechanic_Expertise': expertise,
            'Location': location,
            'Day_of_Week': random.choice(DAYS),
            'Time_of_Day': random.choice(TIMES),
            'Actual_Repair_Hours': hours
        })
    return batch_data

# Generate
b1 = generate_rows(COUNTS['Colombo_Specific'], LOC_COLOMBO_SPECIFIC)
b2 = generate_rows(COUNTS['Colombo_Other'], LOC_COLOMBO_OTHER)
b3 = generate_rows(COUNTS['Matara_Specific'], LOC_MATARA_SPECIFIC)
b4 = generate_rows(COUNTS['Matara_Other'], LOC_MATARA_OTHER)

df = pd.DataFrame(b1 + b2 + b3 + b4)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)
df.insert(0, 'Record_ID', range(1, len(df) + 1))
df.to_csv('suzuki_alto_repair_dataset_real_v7.csv', index=False)

# ==========================================
# 2. STATISTICS
# ==========================================

print("--- 1. Location Statistics ---")
# Count by region (we can infer regions from the lists)
df['Region_Group'] = df['Location'].apply(lambda x: 
    'Colombo Specific' if x in LOC_COLOMBO_SPECIFIC else 
    ('Colombo Other' if x in LOC_COLOMBO_OTHER else 
    ('Matara Specific' if x in LOC_MATARA_SPECIFIC else 'Matara Other')))
print(df['Region_Group'].value_counts())
print("\nTop 10 Locations:")
print(df['Location'].value_counts().head(10))

print("\n--- 2. Mechanic Experience Statistics ---")
print(df['Mechanic_Expertise'].describe())

print("\n--- 3. Fault Category Statistics ---")
print(df['Fault_Category'].value_counts())

print("\n--- 4. Fault Types under Category ---")
print(df.groupby(['Fault_Category', 'Fault_Type']).size())

print("\n--- 5. Severity Statistics ---")
print(df['Severity'].value_counts())

print("\n--- 6. Severity under Fault Types under Category ---")
# Display as a clean text format
grouped_sev = df.groupby(['Fault_Category', 'Fault_Type', 'Severity']).size()
# Just print the first 20 lines to avoid spamming, or print all if requested.
# User asked for statistics, so I'll print a nicely formatted version for a few key ones or summarize.
# Actually, listing all is fine for text output if not too huge.
print(grouped_sev.to_string())

print("\n--- 7. Zero Value Check ---")
print(f"Number of rows with 0.0 Repair Hours: {len(df[df['Actual_Repair_Hours'] == 0.0])}")