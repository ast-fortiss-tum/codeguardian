# Source: Row 850 in ./dataset/CVEfixes/Analysis/results/Python/df_python_all.xlsx

def sync_tree(self):
        LOGGER.info("sync tree to host")

        tree_nodes = self.remove_sensitive_info()
        self.transfer_inst.tree.remote(tree_nodes,
                                       role=consts.HOST,
                                       idx=-1)
        """
        federation.remote(obj=self.tree_,
                          name=self.transfer_inst.tree.name,
                          tag=self.transfer_inst.generate_transferid(self.transfer_inst.tree),
                          role=consts.HOST,
                          idx=-1)
        """