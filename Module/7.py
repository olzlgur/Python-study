from travel import* #외부 파일에서 import
import inspect 

trip_to = thailand.ThailandPackage()
trip_to.detail()

print(inspect.getfile(thailand))