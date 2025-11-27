import streamlit as st
import collections

# Definir el laberinto y puntos de inicio/fin
MAZE = [
    [0,1,0,0,0,0,1,0,0,0],
    [0,1,0,1,1,0,1,0,1,0],
    [0,0,0,0,1,0,0,0,1,0],
    [1,1,1,0,1,1,1,0,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,0,1,0],
    [0,0,0,0,0,0,1,0,1,0],
    [0,1,1,1,1,0,1,0,1,0],
    [0,0,0,0,1,0,0,0,1,0],
    [0,1,1,0,0,0,1,0,0,0]
]

START = (0, 0)
END = (9, 9)

# Algoritmo BFS para resolver el laberinto
def solve_maze_bfs(maze, start, end):
    """Resuelve el laberinto usando el algoritmo de Búsqueda en Amplitud (BFS)."""
    rows, cols = len(maze), len(maze[0])
    queue = collections.deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        (curr_row, curr_col), path = queue.popleft()

        if (curr_row, curr_col) == end:
            return path

        # Movimientos posibles: arriba, abajo, izquierda, derecha
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc
            
            if 0 <= next_row < rows and 0 <= next_col < cols and \
               maze[next_row][next_col] == 0 and (next_row, next_col) not in visited:
                visited.add((next_row, next_col))
                new_path = list(path)
                new_path.append((next_row, next_col))
                queue.append(((next_row, next_col), new_path))
    
    return None  # No se encontró camino

# Configuración de Streamlit
st.set_page_config(page_title="Laberinto BFS", page_icon="🔍", layout="wide")
st.title("🔍 Visualizador de Algoritmo de Búsqueda en Laberinto")

# Función para renderizar el laberinto con iconos de animales
def render_maze_animal(maze, path=None):
    if path is None:
        path = []
    
    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            if (r_idx, c_idx) == START:
                display_row.append("🐰")  # Inicio - Conejo
            elif (r_idx, c_idx) == END:
                display_row.append("🥕")  # Fin - Zanahoria
            elif (r_idx, c_idx) in path:
                display_row.append("🟡")  # Camino resuelto - Amarillo
            elif col == 1:
                display_row.append("🪨")  # Muro - Roca
            else:
                display_row.append("⬜")  # Camino libre - Blanco
        display_maze.append("".join(display_row))
    
    for row in display_maze:
        st.markdown(f"<p style='font-family: monospace; font-size: 20px;'>{row}</p>", unsafe_allow_html=True)

# Función con iconos de aventura
def render_maze_adventure(maze, path=None):
    if path is None:
        path = []
    
    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            if (r_idx, c_idx) == START:
                display_row.append("🧙")  # Inicio - Mago
            elif (r_idx, c_idx) == END:
                display_row.append("🏆")  # Fin - Trofeo
            elif (r_idx, c_idx) in path:
                display_row.append("💎")  # Camino resuelto - Diamante
            elif col == 1:
                display_row.append("🌲")  # Muro - Árbol
            else:
                display_row.append("🟩")  # Camino libre - Verde
        display_maze.append("".join(display_row))
    
    for row in display_maze:
        st.markdown(f"<p style='font-family: monospace; font-size: 20px;'>{row}</p>", unsafe_allow_html=True)

# Función con iconos simples y coloridos
def render_maze_simple(maze, path=None):
    if path is None:
        path = []
    
    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            if (r_idx, c_idx) == START:
                display_row.append("🔵")  # Inicio - Azul
            elif (r_idx, c_idx) == END:
                display_row.append("🟢")  # Fin - Verde
            elif (r_idx, c_idx) in path:
                display_row.append("🟣")  # Camino resuelto - Morado
            elif col == 1:
                display_row.append("⚫")  # Muro - Negro
            else:
                display_row.append("⚪")  # Camino libre - Blanco
        display_maze.append("".join(display_row))
    
    for row in display_maze:
        st.markdown(f"<p style='font-family: monospace; font-size: 20px;'>{row}</p>", unsafe_allow_html=True)

# Función con tema de videojuego
def render_maze_game(maze, path=None):
    if path is None:
        path = []
    
    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            if (r_idx, c_idx) == START:
                display_row.append("👤")  # Inicio - Personaje
            elif (r_idx, c_idx) == END:
                display_row.append("🏰")  # Fin - Castillo
            elif (r_idx, c_idx) in path:
                display_row.append("✨")  # Camino resuelto - Estrellas
            elif col == 1:
                display_row.append("🟫")  # Muro - Marrón
            else:
                display_row.append("🟦")  # Camino libre - Azul
        display_maze.append("".join(display_row))
    
    for row in display_maze:
        st.markdown(f"<p style='font-family: monospace; font-size: 20px;'>{row}</p>", unsafe_allow_html=True)

# Sidebar para controles
st.sidebar.header("🎮 Opciones")

# Selector de tema visual
theme = st.sidebar.selectbox(
    "Selecciona el tema visual:",
    ["Animales", "Aventura", "Simple", "Videojuego"]
)

algorithm = st.sidebar.selectbox(
    "Selecciona el algoritmo:", 
    ["BFS", "DFS (no implementado)", "A* (no implementado)"]
)

solve_button = st.sidebar.button("🔍 Resolver Laberinto")
show_info = st.sidebar.checkbox("📊 Mostrar información detallada", value=True)

# Mostrar información sobre el laberinto
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🧭 Laberinto Actual")
    st.write(f"**Posición de inicio:** {START}")
    st.write(f"**Posición de fin:** {END}")

# Mostrar el laberinto según el tema seleccionado
with col1:
    if theme == "Animales":
        render_maze_animal(MAZE)
    elif theme == "Aventura":
        render_maze_adventure(MAZE)
    elif theme == "Simple":
        render_maze_simple(MAZE)
    elif theme == "Videojuego":
        render_maze_game(MAZE)

# Leyenda de símbolos
with col2:
    st.subheader("📖 Leyenda")
    if theme == "Animales":
        st.write("🐰 = Punto de inicio")
        st.write("🥕 = Punto final")
        st.write("🟡 = Camino solución")
        st.write("🪨 = Muro/Obstáculo")
        st.write("⬜ = Camino libre")
    elif theme == "Aventura":
        st.write("🧙 = Punto de inicio")
        st.write("🏆 = Punto final")
        st.write("💎 = Camino solución")
        st.write("🌲 = Muro/Obstáculo")
        st.write("🟩 = Camino libre")
    elif theme == "Simple":
        st.write("🔵 = Punto de inicio")
        st.write("🟢 = Punto final")
        st.write("🟣 = Camino solución")
        st.write("⚫ = Muro/Obstáculo")
        st.write("⚪ = Camino libre")
    elif theme == "Videojuego":
        st.write("👤 = Punto de inicio")
        st.write("🏰 = Punto final")
        st.write("✨ = Camino solución")
        st.write("🟫 = Muro/Obstáculo")
        st.write("🟦 = Camino libre")

# Resolver el laberinto cuando se presiona el botón
if solve_button:
    if algorithm == "BFS":
        with st.spinner("Buscando camino con BFS..."):
            path = solve_maze_bfs(MAZE, START, END)
        
        if path:
            st.success(f"✅ ¡Camino encontrado con {algorithm}!")
            
            if show_info:
                st.write(f"**Longitud del camino:** {len(path)} pasos")
                st.write(f"**Camino completo:** {path}")
            
            st.subheader("🎯 Laberinto Resuelto")
            
            # Mostrar el laberinto resuelto con el mismo tema
            if theme == "Animales":
                render_maze_animal(MAZE, path)
            elif theme == "Aventura":
                render_maze_adventure(MAZE, path)
            elif theme == "Simple":
                render_maze_simple(MAZE, path)
            elif theme == "Videojuego":
                render_maze_game(MAZE, path)
                
        else:
            st.error("❌ No se encontró un camino desde el inicio hasta el fin.")
    else:
        st.warning(f"⚠️ El algoritmo {algorithm} aún no está implementado. Usa BFS.")

# Información adicional
st.sidebar.markdown("---")
st.sidebar.subheader("ℹ️ Información")
st.sidebar.write("""
**BFS (Breadth-First Search):**
- Explora todos los caminos nivel por nivel
- Garantiza el camino más corto
- Usa una cola (FIFO)
""")