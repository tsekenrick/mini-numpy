# tabletools.py
class LabelledList:
    def __init__(self, data=None, index=None):
        self.values = data
        if index == None:
            self.index = list(range(len(data)))
        else:
            self.index = index
            
    def __str__(self):
        max_len = 0
        # checks for longest length label
        for i in self.values:
            if len(str(self.index[i])) > max_len:
                max_len = len(str(self.index[i]))
        
        max_len += 2
        
        ret_str = ''
        for i, val in enumerate(self.values):
            cur_val = val
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
            
        else:
            return "Query not recognized."
            
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
    
class Table:
    
    def __init__(self, data, index=None, columns=None):
        self.values = data
        if index == None:
            self.index = list(range(len(data)))
        else:
            self.index = index
            
        if columns == None:
            self.columns = list(range(len(data[0])))
        else:
            self.columns = columns
            
    def __str__(self):
        #check for longest length of any item in row, col or val
        max_len = 0
        for i in self.index:
            if len(str(i)) > max_len:
                max_len = len(str(i))
        
        for i in range(len(self.values)):
            for j in self.values[i]:
                if len(str(j)) > max_len:
                    max_len = len(str(j))
                
        for i in self.columns:
            if len(str(i)) > max_len:
                max_len = len(str(i))
        
        max_len += 2 # just some extra padding
        
        #do header row
        col_str = ' ' * max_len
        for i in self.columns:
            col_str += f'{i:>{max_len}}'
        col_str += '\n'
        
        #do the rest
        row_str = ''
        for i, val in enumerate(self.index):
            row_str += f'{val:>{max_len}}'
            for j in self.values[i]:
                row_str += f'{j:>{max_len}}'
            
            row_str += '\n'
            
        return col_str + row_str
            
    def __repr__(self):
        return str(self)
    
    def __getitem__(self, col_list):
        if isinstance(col_list, LabelledList):
            queries = col_list.values
            matches = []
            for i in queries:
                # matches gives indices of matches between self.columns and queries
                matches += [j for j, col in enumerate(self.columns) if col == i]
            
            new_data = [[] for i in range(len(self.values))]
            for i in range(len(self.values)):
                # add the value from the original data for each time its index occurs in matches
                new_data[i] = [self.values[i][idx] for idx in matches]
                
            #creates a clone of queries assuming all elements in queries existed in self.columns
            new_cols = [query for query in queries if query in self.columns]
            
            return Table(new_data, self.index, new_cols)
            
        elif isinstance(col_list, list):
            queries = col_list
            
            #boolean list
            if all(isinstance(query, bool) for query in queries):
                new_data = [[] for i in range(len(self.values))]
                for i in range(len(self.values)):
                    #add value to new data list if its index corresponds to True in queries
                    new_data[i] = [val for j, val in enumerate(self.values[i]) if queries[j] == True]
                    
                new_cols = [col for i, col in enumerate(self.columns) if queries[i] == True]

                return Table(new_data, self.index, new_cols)
            
            #any other list
            else:
                matches = []
                for i in queries:
                    # matches gives indices of matches between self.columns and queries
                    matches += [j for j, col in enumerate(self.columns) if col == i]
            
                new_data = [[] for i in range(len(self.values))]
                for i in range(len(self.values)):
                    # add the value from the original data for each time its index occurs in matches
                    new_data[i] = [self.values[i][idx] for idx in matches]
                
                #creates a clone of queries assuming all elements in queries existed in self.columns
                new_cols = [query for query in queries if query in self.columns]
                
                return Table(new_data, self.index, new_cols)
        
        elif not isinstance(col_list, list):
            query = col_list
            # list of all indices of self.columns that matches query
            matches = [i for i, col in enumerate(self.columns) if col == query]
            if len(matches) == 1:
                return LabelledList([self.values[i][matches[0]] for i in range(len(self.values))], self.index)
            
            elif len(matches) > 1:
                new_data = [[] for i in range(len(self.values))]
                for i in range(len(self.values)):
                    new_data[i] = [self.values[i][idx] for idx in matches]
                    
                new_cols = [query for query in queries if query in self.columns]
                
                return Table(new_data, self.index, new_cols)
            
            else:
                return "No matches for query."
            
        else:
            return "Query not recognized."
    
    def __eq__(self, other):
        if not isinstance(other, Table): 
            return False
        elif self.values != other.values: 
            return False
        elif self.index != other.index:
            return False
        elif self.columns != other.columns:
            return False
        else:
            return True
        
    def __ne__(self, other):
        return not self.eq(other)
    
    def head(self, n):
        new_data = [[] for i in range(n)]
        for i in range(len(new_data)):
            new_data[i] = self.values[i]
            
        new_idx = self.index[:n]
        
        return Table(new_data, new_idx, self.columns)
    
    def tail(self, n):
        new_data = [[] for i in range(n)]
        for i, j in enumerate(range(len(self.values) - n, len(self.values))):
            new_data[i] = self.values[j]
            
        new_idx = self.index[-n:]
        
        return Table(new_data, new_idx, self.columns)
    
    def shape(self):
        return(len(self.index), len(self.columns))
        

def read_csv(fn):
    
            
            