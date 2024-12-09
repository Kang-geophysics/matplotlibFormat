from dataclasses import dataclass

@dataclass
class MatplotlibFormat:
    """
    Author: H.W. Kang
    Class to set the format of matplotlib plots
    Args:
        font_family (str): Font family for the plot
        title_font_size (int): Font size for the title
        label_font_size (int): Font size for the labels
        tick_font_size (int): Font size for the ticks
        legend_font_size (int): Font size for the legend
        grid (bool): Whether to show the grid
        dpi (int): DPI of the plot
    """
    font_family: str = 'Times New Roman'
    title_font_size: int = 15
    label_font_size: int = 12
    tick_font_size: int = 10
    legend_font_size: int = 10
    grid: bool = True
    dpi: int = 100

    def __post_init__(self):
        import matplotlib.pyplot as plt
        plt.rcParams['font.family'] = self.font_family
        plt.rcParams['font.size'] = self.label_font_size
        plt.rcParams['xtick.labelsize'] = self.tick_font_size
        plt.rcParams['ytick.labelsize'] = self.tick_font_size
        plt.rcParams['legend.fontsize'] = self.legend_font_size
        plt.rcParams['axes.grid'] = self.grid
        plt.rcParams['figure.dpi'] = self.dpi
    
    def __str__(self):
        return f'font_family: {self.font_family}\n title_font_size: {self.title_font_size}, label_font_size: {self.label_font_size}, tick_font_size: {self.tick_font_size}, legend_font_size: {self.legend_font_size}, grid: {self.grid}, dpi: {self.dpi}'
    
if __name__ == '__main__':
    format = MatplotlibFormat()
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Sine wave')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.legend(['sin(x)'])
    plt.show()
    print(format)



