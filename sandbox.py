

def warn_the_sheep(queue):
    if queue[-1] == 'wolf':
        print("Pls go away and stop eating my sheep")
    elif 'wolf' in queue:
        wolf_index = queue.index('wolf')
        print(f"Oi! Sheep number {len(queue) -1 - wolf_index}! You are about to be eaten by a wolf!")
    


queue = ['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']
# Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"

# queue = ["sheep", "sheep", "wolf"]
# Output: "Pls go away and stop eating my sheep"

warn_the_sheep(queue)

print("Comment for the days")





















































