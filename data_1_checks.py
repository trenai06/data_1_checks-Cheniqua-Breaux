print ("Hello, World")
Ingredients = ["Water", "Dry Active Yeast", "Olive Oil", "Bread Flour", "Sugar", "Salt"]
print (Ingredients)
print(len(Ingredients))
Batch = [ 
    {
    "Yield" : 1,    
    "Water" : 454, 
    "Dry Active Yeast" : 10,
    "Bread Flour" : 348,
    "Sugar" : 9, 
    "Salt" : 3,
    "Olive Oil" : 13},
{
    "Yield" : 2,
    "Water" : 908, 
    "Dry Active Yeast" : 20, 
    "Bread Flour" : 696, 
    "Sugar" : 18, 
    "Salt" : 6, 
    "Olive Oil" : 26}, 
{
    "Yield" : 3, 
    "Water" : 1362, 
    "Dry Active Yeast" : 30, 
    "Bread Flour" : 1044, 
    "Sugar" : 27,
    "Salt" : 9, 
    "Olive Oil" : 39
}
]
print (Batch [0])
print (type (Batch[0]))
print (Batch[0] ["Bread Flour"])

