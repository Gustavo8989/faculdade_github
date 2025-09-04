#include <iostream> 
using namespace std;

void hashmap_insere(HashMapa *hashmapa, unsigned int key, int valor){
    unsigned int hash = hashmapa_hash_func(hashmapa,key);
    HashmapNo *hashmap_node = hashmapa -> node_list[hash];
    if (hashmap_node != NULL && hashmapa -> node_list[hash] -> hash_index == key){
        hashmapa_remove(hashmap, key);
    }
    hashmap_node = hashmapa_new_node(hash, valor);
    hashmap -> cont_elementos++; 

