import torch

def main():
    list = [[1,2,3],[4,5,6]]
    xt = torch.tensor(list)
    print(xt)
    print(xt.shape)

    print("=========")
    yt = torch.tensor(3.)
    print(yt)
    print(yt.shape)

    print("=========")
    m = torch.ones(3,3,3)
    print(m)

if __name__ == "__main__":
    main()