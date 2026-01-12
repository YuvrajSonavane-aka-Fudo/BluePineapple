
#!write a user form having fields id , name , age , email and handle exceptions

userId = int(input("Please enter id"))
name = input("Please enter name")
age = int(input("Please enter age"))
email = input("Please enter email")

def handle_user_form(id , name , age , email):
    try:
        if not isinstance(id , (int,float)):
            raise TypeError
        if name == "":
            raise NameError
        if age < 0 or age >100:
            raise ValueError 
        if "." not in email or "@" not in email:
            raise NameError

        return "all checks passed"

    except TypeError:
        return "Invalid Id"
    except NameError:
        return "There might be a mistake in the name or email"
    except ValueError:
        return "Please enter age between 1 and 100"
    except Exception:
        return "An unexpected error occured"
    
    finally:
        return "finally block"
    
print(handle_user_form(userId , name , age , email))
        
        





