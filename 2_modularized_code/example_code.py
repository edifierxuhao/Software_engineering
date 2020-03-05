from Gaussiandistribution import Gaussian

gaussian_three = Gaussian()
gaussian_three.read_data_file('numbers.txt')

print(gaussian_three.calculate_stdev())
gaussian_three.plot_histogram_pdf()
