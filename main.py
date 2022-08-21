import sys
from repository import repo
import DTO


def main():
    repo.create_tables()

    # parsing config file
    with open(sys.argv[1]) as config:
        lines = config.readlines()
        index = 1
        num_of_each = lines[0].split(",")
        hats = lines[index: index + int(num_of_each[0])]
        index = index + int(num_of_each[0])
        suppliers = lines[index:index + int(num_of_each[1])]
        for line in hats:
            line = line.replace("\n", "")
            args = line.split(",")
            repo.hat_dao.insert(DTO.Hat(int(args[0]), args[1], int(args[2]), int(args[3])))
        for line in suppliers:
            line = line.replace("\n", "")
            args = line.split(",")
            repo.supplier_dao.insert(DTO.Supplier(int(args[0]), args[1]))

    # executing orders from orders file
    with open(sys.argv[2]) as orders, open(sys.argv[3], "w") as output:
        lines = orders.readlines()
        for line in lines:
            line = line.replace("\n", "")
            args = line.split(",")
            topping, supplier, location = repo.execute_order(args[0], args[1])
            output.write("{},{},{}\n".format(topping, supplier, location))


if __name__ == '__main__':
    main()
