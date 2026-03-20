try:
    with open('canciones.txt', 'r', encoding='utf-8') as file:
        songs = [line.strip() for line in file.readlines()]
        
    songs.sort()
        
    with open('canciones_ordenadas.txt', 'w', encoding='utf-8') as final_file:
            for song in songs:
                final_file.write(song + '\n')
                
    print(f'Las canciones se han guardado en {"canciones_ordenadas.txt"}')
        
except FileNotFoundError:
    print(f'No se enccontró el archivo {'canciones.txt'}')