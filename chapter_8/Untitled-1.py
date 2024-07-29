def print_models(unprinted_designes, completed_designs):
    while unprinted_designes:
        current_design = unprinted_designes.pop()
        print(f"printing model: {current_design}")
        completed_designs.append(current_design)
def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in  completed_models:
        print(completed_model)

unprinted_designs = ['phone_case', 'robot pendant', 'dodecahedron']
completed_designs = []

print_models(unprinted_designes= unprinted_designs[:], completed_designs= completed_designs)

show_completed_models(completed_models= completed_designs)