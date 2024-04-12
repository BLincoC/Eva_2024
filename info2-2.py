def main():
  """
  Actividad 4 Prueba Numero 1 Redes virtualizadas.
  """
  vlan_id = int(input("Inserta tu VLAN ID: "))

  if 1 <= vlan_id <= 1005:
    print(f"La VLAN {vlan_id} corresponde aun rango normal")
  elif 1006 <= vlan_id <= 4095:
    print(f"La VLAN {vlan_id} corresponde aun rango extendido")
  else:
    print(f"La VLAN ingresada {vlan_id} resulta desconocida.")

if __name__ == "__main__":
  main()