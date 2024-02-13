# Exercise Name:
# 	08-Decorator-Demo
# Description:
# 	Create a decorator called 'time_this' and use it to measure time taken to run functions

# For example, running:
# 	@time_this
# 	def sleeper_func(sleeptime):
# 	    print(f'sleeping for {sleeptime}')
# 	    sleep(sleeptime)
# 	    return 'Woke up!'

# 	sleeper_func(2)

# Should output the following in the console:
# 	--> Running sleeper_func
# 	sleeping for 2
# 	--> sleeper_func ran in 2.002105236053467 seconds
import time

def time_this(sleeper_func):
    def wrapped_func(sleeptime):
        begin = time.time()

        return_val = sleeper_func(sleeptime)
        end = time.time()

        print("Total time taken is : ", end - begin)

        return return_val
    return wrapped_func

@time_this
def sleeper_func(sleeptime):
    print(f'sleeping for {sleeptime}')
    time.sleep(sleeptime)
    return 'Woke up!'

sleeper_func(2)

