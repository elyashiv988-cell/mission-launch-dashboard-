#namber 2
agent_name= "david cohen"
mission_code= 693
distance_to_target= 5.5
mission_status= False
#namber 3
print(f"agent name: {agent_name} ,mission_code : {mission_code} , distance to target: {distance_to_target}k.m , mission status: {mission_status}")
#namer 4
print(type(agent_name))
print(type(mission_code))
print(type(distance_to_target))
print(type(mission_status))
#namber 5
base_to_target_and_back=distance_to_target*2
print(f"distans of trip: {base_to_target_and_back}")
#namber 6
fuel_usage=3
fuel_usage=int(fuel_usage)
fuel_usage_for_mission=base_to_target_and_back*fuel_usage
print(f"fuel usage for mission: {fuel_usage_for_mission}")
#namer 7
total_fuel=50
total_fuel=int(total_fuel)
total_fuel_after_mission=total_fuel-fuel_usage_for_mission
print(f"total fuel after mission: {total_fuel_after_mission}")
#namber 8
time=input("in how many minutes does the mission start ?")
time=int(time)
print(f"the mission starts in {time*60} secends")
print(f"the mission starts in {time} minutes")
print(f"the mission starts un {time/60} houres")
# namber 9
d_km= input("enter distance in k.m")
d_km= int(d_km)
mail= d_km/1.6
print(f"the distance is {mail} mails")
#namber 10
new_agent_name=input("enter your agent name")
print(f"agent A {agent_name} , agent B {new_agent_name}")