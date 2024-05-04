# We have a list of products and our task is to write a program
# that finds out if entered by the user product is present in the list or not

products = [
    'apples',
    'bananas',
    'coffee',
    'cheese',
    'sausages',
    'spaghetti']

for x in range(5):
    search = input()
    matches = []
    for product in products:
        if search in product:
            matches.append(product)

    count = len(matches)
    if count == 0:
        print(f'No matches found for {search}!')
    else:
        print(f'{count} matches found for {search}:')
        for match in matches:
            print('  ', match)
