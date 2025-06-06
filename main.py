from utils import *

def main():
    #Getting informations from the user (path of input and output files and the parameter K - groups amount)
    fp_input = input("Forneca o nome do arquivo de entrada: ")
    fp_output = input("Forneca o nome do arquivo de saida: ")
    K = int(input("Forneca o número de grupos (K): "))

    #Reading point informations (coordinates and dimensions) from CSV file
    points = read_csv(fp_input)

    #Calculating distances between points and building the links
    links = build_links(points)

    #Cutting the K largest links
    cut_links_list = cut_links(links, K)

    #Organizing groups from cut links
    groups = build_groups(cut_links_list, points)

    #Saving the groups in output file
    save_output(fp_output, groups)

    #Printing the groups
    print_groups(groups)

if __name__ == "__main__":
    main()