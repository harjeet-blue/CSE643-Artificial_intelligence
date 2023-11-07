import json

def read_knowledge_base():
    with open('knowledge_base.json', 'r') as json_file:
        knowledge_base = json.load(json_file)

    return knowledge_base


def add_new_destination():
    new_destinations = {}

    # Ask the user for new destinations
    destination = input("Enter a destination: ").strip()

    # Read the existing knowledge base
    existing_kb = read_knowledge_base()

    # Check if the destination exists
    if destination in existing_kb:
        print("Destination already exists. Add a feedback instead (y/n).")
        choice = input().strip().lower()
        if choice == "y":
            add_feedback()
        return

    new_destinations[destination] = {
        "weather": None,
        "activities": None,
        "connectivity": None,
        "budget": None,
        "distance": None,
        "feedbacks": None,
        "rating": None,
    }

    weather = input("What is the weather like? (Hot, Varied, Mild, Cold) ")
    activities = input("What activities are there? ").split(" ")
    connevtivity = input("What is the connectivity like? (Air, Road, Water) ").split(" ")
    budget = input("What is the budget like? (Moderate, High-End, Budget-Friendly) ")
    distance = input("What is the distance like? (Long-haul, Short-haul) ")
    feedback = input("What is the feedback like? ")
    rating = int(input("What is the rating like? (1-10) "))


    new_destinations[destination]["weather"] = weather
    new_destinations[destination]["activities"] = activities
    new_destinations[destination]["connectivity"] = connevtivity
    new_destinations[destination]["budget"] = budget
    new_destinations[destination]["distance"] = distance
    new_destinations[destination]["feedbacks"] = [feedback]
    new_destinations[destination]["rating"] = [rating]


    existing_kb.update(new_destinations)

    # Save the destination to the knowledge base
    with open('knowledge_base.json', 'w') as json_file:
        json.dump(existing_kb, json_file, indent=4)


def add_feedback():

    while True:
        # Ask the user for the destination
        destination = input("Enter a destination: ").strip()

        # Read the existing knowledge base
        existing_kb = read_knowledge_base()

        # Check if the destination exists
        if destination in existing_kb:
            feedback = input("What is the feedback like? ")
            rating = int(input("What is the rating like? (1-10) "))

            existing_kb[destination]["feedbacks"].append(feedback)
            existing_kb[destination]["rating"].append(rating)

            # Save the destination to the knowledge base
            with open('knowledge_base.json', 'w') as json_file:
                json.dump(existing_kb, json_file, indent=4)

            break
        else:
            print("Destination not found. Please try again.")


def check_feedbacks():
    while True:
        # Ask the user for the destination
        destination = input("Enter a destination: ").strip()

        # Read the existing knowledge base
        existing_kb = read_knowledge_base()

        # Check if the destination exists
        if destination in existing_kb:
            print("Feedbacks: ")
            print(existing_kb[destination]["feedbacks"])
            print("Ratings: ")
            print(existing_kb[destination]["rating"])
            print("Average rating: ")
            print(sum(existing_kb[destination]["rating"]) / len(existing_kb[destination]["rating"]))
            break
        else:
            print("Destination not found. Please try again.")


def pretty_print_dict(d, indent=0):
    for key, value in d.items():
        if isinstance(value, dict):
            print(' ' * indent + f"{key}:")
            pretty_print_dict(value, indent + 2)
        else:
            print(' ' * indent + f"{key}: {value}")


def recommend_destination_backtracing(questions, destinations, existing_kb):
    # Base case
    if len(questions) == 0 or len(destinations) == 0:
        return destinations

    # Recursive case
    question = questions.pop(0)

    while True:
        # Ask the user for the answer
        answer = input("Enter your " + question + " preference :-").strip()

        # Filter the destinations based on the answer
        filter_destinations = [destination for destination in destinations if existing_kb[destination][question] == answer]

        options = recommend_destination_backtracing(questions, filter_destinations, existing_kb)

        if len(options) > 0:
            break
        else:
            print("\nNo destinations found.")
            print("possible options are: ")
            
            possible_options = set()

            for destination in destinations:
                possible_options.add(existing_kb[destination][question])
            
            print(possible_options)

            choice = input("Try again (y). Go back to previous question (n). (y/n) ").strip().lower()
            if choice == "n":
                break

    return options


def recommend_destination():

    print("\nAnswer the following questions to get a recommendation.")

    print("Types of weather: { Hot, Varied, Mild, Cold }")
    print("Types of budget: { Moderate, High-End, Budget-Friendly }")
    print("Types of distance: { Long-haul, Short-haul }\n")


    # Read the existing knowledge base
    existing_kb = read_knowledge_base()

    destinations = list(existing_kb.keys())

    questions = ["weather", "budget", "distance"]

    recom = recommend_destination_backtracing(questions, destinations, existing_kb)

    print("\nRecommended destinations: ")
    for destination in recom:
        print(destination)
        pretty_print_dict(existing_kb[destination])
        print()


def main():
    while True:
        print("\n1. Add a new destination")
        print("2. Add a feedback and rating for a destination")
        print("3. Destination recommendation based on preferences")
        print("4. Check feedbacks and ratings for a destination")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_new_destination()
        elif choice == 2:
            add_feedback()
        elif choice == 3:
            recommend_destination()
        elif choice == 4:
            check_feedbacks()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Try again.")



if __name__ == "__main__":
    main()