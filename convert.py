import argparse


def main():
    parser = argparse.ArgumentParser(description='用于 Android Strings 转化',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-m', dest='module', action='store', type=str, required=True, default='ExcelToXml',
                        help='模块名，ExcelToXml and XmlToExcel')
    args = parser.parse_args()

    module = args.module
    print(module)


if __name__ == '__main__':
    main()
