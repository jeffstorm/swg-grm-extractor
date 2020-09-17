#!/usr/bin/env python

"""
This tool allows for users to scrape data and generate a pickle file containing
all actual resources from the specified SWG server.
"""

from __future__ import print_function
import os
import sys
import argparse

from utils import print_server_list, get_resources, get_resources_classes, get_resources_mapping, aggregate_classes, print_classes

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--list-servers', help="Put this flag to simply list the available servers. This overrides other flags.",
                        action='store_true', default=False)
    parser.add_argument('-r', '--refresh_data', help="Put this flag to refresh the resources classes list. This overrides other flags.", action='store_true', default=False)
    parser.add_argument('-v', '--view_classes', help="Read the classes list.", action='store_true', default=False)
    parser.add_argument('-u', '--url', help="This value can override the default url (SWGAide) not recommended since this tool is designed to work with SWGAide.",
                        type=str, default='https://swgaide.com/')
    parser.add_argument(
        '-s', '--server', help="The SWG server number. Use flag '--list-servers' to find your server.", type=int, required=True)
    # TODO: add the possibility to override the output file.
    # parser.add_argument('-o', '--outfile', help="The output file to generate the resources.", 
    #                    default='resources.pickle', type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    if args.list_servers:
        print_server_list(args.url)
    elif args.view_classes:
        print_classes()
    elif args.refresh_data or not os.path.isfile('swg-grm-extractor/data/classes.pkl'): 
        classes = get_resources_classes('http://www.swgcraft.org/')
        mapping = get_resources_mapping('http://www.swgcraft.org/')
        aggregate_classes(classes, mapping) 
    else:
        get_resources(args.url, args.server)

    # get_resources(args.url, args.server) if not args.list_servers else 
    
    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
