vignesh_choice, charan_choice = input().split()
if vignesh_choice == charan_choice:
    print("NULL")
elif (vignesh_choice == 'R' and charan_choice == 'S') or \
     (vignesh_choice == 'P' and charan_choice == 'R') or \
     (vignesh_choice == 'S' and charan_choice == 'P'):
    print("Vignesh")
else:
    print("Charan")
