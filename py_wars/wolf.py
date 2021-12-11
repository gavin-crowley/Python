def warn_the_sheep(queue):
    n = len(queue) - queue.index('wolf') - 1
    return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'


#my attempt

def warn_the_sheep(queue):
    if queue[-1] == 'wolf':
        print("Pls go away and stop eating my sheep")
    elif 'wolf' in queue:
        wolf_index = queue.index('wolf')
        print(f"Oi! Sheep number {len(queue) -1 - wolf_index}! You are about to be eaten by a wolf!")