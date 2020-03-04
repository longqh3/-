class GTEx_parser(object):
    def __init__(self, GTEx_database_loc):
        self.GTEx_database = open(GTEx_database_loc)
    # Output: Dict
    # Contents: Tissue and corresponding p value for each SNP
    def GTExDictCreate(self):
        # Title excluded
        try:
            GTEx_dict = {}
            tissue_all_info = set()
            title = self.GTEx_database.readline().rstrip()
            while True:
                line = self.GTEx_database.readline().rstrip()
                if line:
                    [Gencode_ID, Gene_Symbol, Variant_ID, SNP_ID, P_value, NES, Tissue] = [str(info) for info in line.split(",")]
                    tissue_all_info.add(Tissue)
                    if not GTEx_dict.__contains__(SNP_ID):
                        GTEx_dict[SNP_ID] = {}
                        GTEx_dict[SNP_ID][Tissue] = P_value
                    else:
                        GTEx_dict[SNP_ID][Tissue] = P_value
                else:
                    print("GTEx gene info has been read into memory")
                    print("The number of relevant tissues is %d" % len(tissue_all_info))
                    break
        except Exception as e:
            print(e.args)
        finally:
            self.GTEx_database.close()
            return GTEx_dict, tissue_all_info
    # Output: print info
    def GTExDictWrite(self, GTEx_dict, tissue_all_info):
        # set select criteria
        print("Here're %d SNPs that correlate with all available tissues below" % (len(GTEx_dict)))
        print(tissue_all_info)
        for SNP_ID in GTEx_dict.keys():
            # only select SNP that contains all tissue
            # if len(GTEx_dict[SNP_ID]) == len(tissue_all_info):
            #     print(SNP_ID)
            print(SNP_ID, len(GTEx_dict[SNP_ID]))
    def run(self):
        GTEx_dict, tissue_all_info = self.GTExDictCreate()
        self.GTExDictWrite(GTEx_dict, tissue_all_info)

if __name__ == '__main__':
    gtex = GTEx_parser("C:\\Users\\qihan\\Desktop\\GTEx Portal_TMPRSS2.csv")
    gtex.run()