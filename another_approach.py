
API_KEY = 'AIzaSyAwwe6Z2eV_xIa7g7kWo4T7uIFtLgn1nkY'


file_id = '1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ'
folder_id = '0BwwA4oUTeiV1TGRPeTVjaWRDY1E'
# Retrieve the existing parents to remove
file = drive_service.files().get(fileId=file_id,
                                 fields='parents').execute()
previous_parents = ",".join(file.get('parents'))
# Move the file to the new folder
file = drive_service.files().update(fileId=file_id,
                                    addParents=folder_id,
                                    removeParents=previous_parents,
                                    fields='id, parents').execute()
