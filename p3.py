import pickle

def load_data(file):
    # file is the name of data file (e.g., \texttt{dept-prof.pydata})
    # Enter your code here
    result = {}
    try:
        with open(file, 'rb') as f:
            result = pickle.load(f)
    except IOError as e:
        print('unable to open the file with error: "{}"'.format(e.args[-1]))
    except Exception as e:
        print(e)

    return result

def query(prof_name):
    # Enter your code here
    result = []
    data = {}
    data = load_data('dept-prof.pydata')
    for dept in data:
        if prof_name in data[dept]:
            result.append(dept)
    return [x for x in data if prof_name in data[x]]

def update():
    # Enter your code here
    data = {}
    data = load_data('dept-prof.pydata')
    data['Computer Science'] += data['Artificial Intelligence']
    del data['Artificial Intelligence']
    data['Space Engineering'] = ['Mark', 'Neo', 'Jane']
    try:
        with open('dept-prof-updated.pydata', 'wb') as fout:
            pickle.dump(data, fout)
    except IOError as e:
        print('unable to open the file with error: "{}"'.format(e.args[-1]))
    except Exception as e:
        print(e)

def get_depts_size():
    # Enter your code here
    result = {}
    result = load_data('dept-prof-updated.pydata')
    for dept in result:
        result[dept] = len(result[dept])
    return result

if __name__ == "__main__":
    # you can test your function by using the following
    dept_prof = load_data('dept-prof.pydata')
    print(dept_prof)

    depts = query('John')
    print(depts)

    dept_prof = update()

    dept_size = get_depts_size()
    print(dept_size)