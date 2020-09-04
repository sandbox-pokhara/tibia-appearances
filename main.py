'''Main module'''
import argparse

from google.protobuf.json_format import MessageToJson

import appearances_pb2

parser = argparse.ArgumentParser()
parser.add_argument('appearances_dat')
parser.add_argument('output')
args = parser.parse_args()


def main():
    '''Main function'''
    appearances = appearances_pb2.Appearances()
    with open(args.appearances_dat, 'rb') as file_pointer:
        appearances.ParseFromString(file_pointer.read())
    with open(args.output, 'w') as file_pointer:
        file_pointer.write(MessageToJson(appearances))


if __name__ == '__main__':
    main()
