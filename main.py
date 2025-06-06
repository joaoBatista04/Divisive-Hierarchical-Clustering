from utils import *

def main():
    fp_input = input("Forneca o nome do arquivo de entrada: ")
    fp_output = input("Forneca o nome do arquivo de saida: ")
    K = int(input("Forneca o número de grupos (K): "))

    points = read_csv(fp_input)

    links = build_links(points)

    cut_links_list = cut_links(links, K)

    groups = build_groups(cut_links_list, points)
    
    print_groups(groups)

    save_output(fp_output, groups)

if __name__ == "__main__":
    main()