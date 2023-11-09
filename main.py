import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('Agg')


class CityGrid:
    def __init__(self, N, M, obstacle_coverage):
        self.N = N
        self.M = M
        self.grid = np.zeros((N, M))
        self.place_obstacles(obstacle_coverage)

    def place_obstacles(self, obstacle_coverage):
        num_obstacles = int(obstacle_coverage * self.N * self.M)
        indices = np.random.choice(self.N * self.M, num_obstacles, replace=False)
        self.grid.flat[indices] = 1

    def place_tower(self, row, col, radius):
        # Mark the tower on the grid
        self.grid[row, col] = 2  # 2 represents tower

        cmap = plt.get_cmap('tab10')
        tower_color = cmap(6)
        plt.scatter([col], [row], color=[tower_color], marker='s', s=100, linewidths=2, edgecolors='black', label='Tower')

        # Mark the coverage area of the tower
        for i in range(max(0, row - radius), min(self.N, row + radius + 1)):
            for j in range(max(0, col - radius), min(self.M, col + radius + 1)):
                self.grid[i, j] = max(self.grid[i, j], 3)  # 3 represents coverage area

    def visualize_grid(self):
        cmap = plt.get_cmap('tab10')
        bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
        norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N, clip=True)

        plt.imshow(self.grid, cmap=cmap, norm=norm, interpolation='nearest')

        # Add a custom colorbar
        cbar_ticks = [0, 1, 2, 3]
        cbar_labels = ['Free Block', 'Blocked Block', 'Tower', 'Coverage Area']
        cbar = plt.colorbar(ticks=cbar_ticks)
        cbar.ax.set_yticklabels(cbar_labels)

        plt.title('City Grid')
        plt.savefig('city_grid.png')


# Пример использования:
city = CityGrid(20, 20, 0.3)
city.place_tower(8, 4, 2)
city.visualize_grid()
