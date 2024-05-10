import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test')

    # basic config
    parser.add_argument('--name', type=str, default='zzz')
    parser.add_argument('--age', type=int, default=12)
    parser.add_argument('--gender', type=str, default='male')

    args = parser.parse_args()
    print(f'{args.name} {args.age}')