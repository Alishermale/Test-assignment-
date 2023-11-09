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
        # Randomly place blocked blocks with given coverage
        num_obstacles = int(obstacle_coverage * self.N * self.M)
        indices = np.random.choice(self.N * self.M, num_obstacles, replace=False)
        self.grid.flat[indices] = 1

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
city.visualize_grid()
