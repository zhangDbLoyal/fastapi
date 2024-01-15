from fdfs_client.client import get_tracker_conf, Fdfs_client






if __name__ == '__main__':
    tracker_conf = {'host_tuple': ("10.0.47.165:22122",), 'port': 48080, 'timeout': 601, 'name': 'Tracker Pool'}
    client = Fdfs_client(tracker_conf)
    print(client.list_all_groups())
