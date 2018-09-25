# tabletools.py
class LabelledList:
    def __init__(self, data=None, index=None):
        self.values = data
        if index == None:
            self.index = list(range(len(data)))
        else:
            self.index = index
            
    def __str__(self):
        #check for label of highest length
        max_len = 0
        for i in self.values:
            if len(str(self.index[i])) > max_len:
                max_len = len(str(self.index[i]))
        
        ret_str = ''
        for i in self.values:
            cur_val = self.values[i]
            cur_idx = self.index[i]
            ret_str += f'{cur_idx:>{max_len}}   {cur_val}\n'
            
        return ret_str
        
    def __repr__(self):
        return str(self)
    
    def __getitem__(self, key_list):
        # labelledlist passed as arg
        if isinstance(key_list, LabelledList):
            queries = key_list.values
            keys = self.index # labels for this labeledlist
            matches = []
            for i in queries:
                # matches gives indices of matches between self.index and queries
                matches += [j for j, key in enumerate(keys) if key == i]
                # flat_list = [item for sublist in l for item in sublist] try this if need append
            new_values = []
            new_index = []
            
            for i in matches:
                new_values.append(self.values[i])
                new_index.append(self.index[i])
                
            new_ll = LabelledList(new_values, new_index)
            return new_ll
        
        #list passed as arg
        elif isinstance(key_list, list):                                                         
            
            #list is boolean
            if all(isinstance(key, bool) for key in key_list):
                new_values = []
                new_index = []
                for i, key in enumerate(key_list):
                    if(key == True):
                        new_values.append(self.values[i])
                        new_index.append(self.index[i])
                
                new_ll = LabelledList(new_values, new_index)
                return new_ll
            
            #list is non-boolean
            else:
                keys = self.index # labels for this labeledlist
                matches = []
                for i in key_list:
                    # matches gives indices of matches between self.index and queries
                    matches += [j for j, key in enumerate(keys) if key == i]
                    # flat_list = [item for sublist in l for item in sublist] try this if need append
            
                new_values = []
                new_index = []
            
                for i in matches:
                    new_values.append(self.values[i])
                    new_index.append(self.index[i])
                
                new_ll = LabelledList(new_values, new_index)
                return new_ll
        
        #single value as arg
        elif not isinstance(key_list, list):
            keys = self.index
            matches = []
            matches += [i for i, key in enumerate(keys) if key == key_list]
            
            if len(matches) > 1:
                new_values = []
                new_index = []
                
                for i in matches:
                    new_values.append(self.values[i])
                    new_index.append(self.index[i])
                    
                new_ll = LabelledList(new_values, new_index)
                return new_ll
            
            elif len(matches) == 1:
                return self.values[matches[0]]
            
            else:
                return "No matches for query."
            
    def __setitem__(self, key, value):
        matches = []
        keys = self.index
        matches += [i for i, label in enumerate(keys) if label==key]
        
        for i in matches:
            self.values[i] = value
            
    def __iter__(self):
        return self.values
    
    def __eq__(self, scalar):
        bool_list = [i==scalar for i in self.values]
        return LabelledList(bool_list, self.index)
    
    def __ne__(self, scalar):
        bool_list = [i!=scalar for i in self.values]
        return LabelledList(bool_list, self.index)
    
    def __gt__(self, scalar):
        bool_list = [i>scalar for i in self.values]
        return LabelledList(bool_list, self.index)
    
    def __lt__(self, scalar):
        bool_list = [i<scalar for i in self.values]
        return LabelledList(bool_list, self.index)
    
    def map(self, f):
        new_vals = [f(i) for i in self.values]
        return LabelledList(new_vals, self.index)