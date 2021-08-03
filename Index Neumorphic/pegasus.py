import os


    
while True:
    try:
        file = input("Enter the file names: =>")
        # os.remove(file)

        if file == 'exit':
            break
        if file.endswith('.py','.html'):
            os.remove(file)
        else:
            print("This is not Python File!!!!")
    except Exception as e:
        print(e)