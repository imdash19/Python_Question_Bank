# Write a Python program to get effective group id,
# effective user id, real group id,
# and list of supplemental group ids.
# Note: Unix only

import os

def get_process_ids():
    try:
        effective_uid = os.geteuid()
        effective_gid = os.getegid()
        real_gid = os.getgid()
        supplemental_groups = os.getgroups()

        print("\n--- Process Identity Information ---\n")
        print("Effective User ID (EUID):", effective_uid)
        print("Effective Group ID (EGID):", effective_gid)
        print("Real Group ID (GID):", real_gid)
        print("Supplemental Group IDs:", supplemental_groups)

    except AttributeError:
        print("This program is only supported on Unix/Linux systems.")

get_process_ids()