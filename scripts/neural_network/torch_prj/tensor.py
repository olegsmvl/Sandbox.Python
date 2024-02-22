import torch

def main():
    list = [[1,2,3],[4,5,6]]
    xt = torch.tensor(list).float()
    print(xt)
    print(xt.shape)

    # print("=========")
    # yt = torch.tensor(3.)
    # print(yt)
    # print(yt.shape)
    #
    # print("=========")
    # m = torch.ones(3,3,3)
    # print(m)

    print("=========")
    m = torch.ones(3,2)
    m = m*2
    print(m)
    print(m.shape)
    mul = torch.mm(xt, m)
    print(mul)

if __name__ == "__main__":
    main()