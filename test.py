def dynamic_field_mapping(input_data):
    # Define keyword mappings to standard attributes
    keyword_mappings = {
        "PlayerFirstName": ["player", "first"],
        "PlayerLastName": ["player", "last"],
        "PlayerRanking": ["player", "rank"],
        "PlayerERA": ["era"],
        "PlayerEmail": ["coach", "email"]
        # Add other mappings as needed
    }

    # Helper function to check if all keywords are in the field name
    def matches_keywords(field_name, keywords):
        field_name_lower = field_name.lower()
        return all(keyword in field_name_lower for keyword in keywords)

    # Generate output with dynamic mapping based on keyword matching
    output_data = {}
    for input_key, value in input_data.items():
        matched = False
        for standard_key, keywords in keyword_mappings.items():
            if matches_keywords(input_key, keywords):
                output_data[standard_key] = value
                matched = True
                break
        if not matched:
            output_data[input_key] = value  # Use original key if no match found

    return output_data

# Example input data
input_data = {
    "Name of player (first)": "John",
    "Name of player (last)": "Doe",
    "player's first name": "Jane",  # This will also match to PlayerFirstName
    "ERA statistics": 2.85,  # This will match to PlayerERA
    "Club Coach Email Address": "coach@email.com"
}

# Process the input data with dynamic mapping
processed_data = dynamic_field_mapping(input_data)
print(processed_data)
