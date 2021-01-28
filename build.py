# @Author: Liona Maskros <lionacc@163.com>
# @Date: 2021-01-27 12:20:33
# @Last Modified by: Liona Maskros <lionacc@163.com>
# @Last Modified time: 2021-01-27 22:46:04

import markdown
from rich.console import Console
import os
import uuid
import json
import requests


class Make_date(object):
    """Make the markdown filetype to Json filetype

    Use python-markdown and it's extensions to convert markdown file
    into Json file and include the front meta info. while do this work
    will make HTML content and put it into Json file

    """
    def __init__(
        self,
        markdown_store_dir,
        store_path,
        repos_api,
        about_md_file="About.md",
    ):
        """
        Args:
            markdown_store_dir (path): the path of markdown file
            store_path (path): Json file will save
            repos_api (str): the github api url to requests the user info
            about_md_file (str): the about me markdown file name
        """

        self.store_path = store_path
        self.repos_api = repos_api
        self.markdown_store_dir = markdown_store_dir
        self.about_md_file = markdown_store_dir + about_md_file
        self.about_json_file_path = store_path + "about.json"
        self.blog_all_list_json_file_path = store_path + "blog_all_list.json"
        self.repos_list_json_file_path = store_path + "repos_list.json"

        self.blog_all_list_data = {}  #
        self.blog_alt_path_list = []
        self.blog_tag_list = []
        self.blog_categary_list = []
        self.blog_date_list = []

        self.console = Console()
        self.console.log(self.console)

        self.extensions = [
            "toc",
            "codehilite",
            "footnotes",
            "meta",
            "fenced_code",
            "tables",
            "smarty",
        ]

    def make_blog_all_list(self):
        """make markdown file info into one Json file"""

        for path, dir_list, file_list in os.walk(markdown_store_dir):
            for file_name in file_list:
                self.console.log(path, file_name)
                if file_name != ".DS_Store":
                    md_file_path = os.path.join(path, file_name)
                    self.md2json(md_file_path,
                                 self.blog_all_list_json_file_path, False)
                else:
                    pass
        # self.console.log(data)
        self.console.log("Local markdown file covert completed.")

    def make_repos_list(self):
        """requests gtihub api and store the response"""
        data = {}
        response = requests.get(repos_api)
        data = response.text
        with open(self.repos_list_json_file_path, "w",
                  encoding="utf-8") as file:
            file.write(data)
        self.console.log("Repos information get successfully.")

    def make_about_page(self):
        """convert About.md"""
        self.md2json(self.about_md_file, self.about_json_file_path)
        self.console.log("About me page make completed.")

    def md2json(self, md_file_path, json_file_path="", content=True):
        """main program

        main program to realize convert function

        Args:
            md_file_path (path): the markdown file import from
            json_file_path (path): the json file will save to

        Returns:
            dict: the markdown file content

        Raises:
            the path is wrong

        """
        data = {}
        with open(md_file_path) as md_file:
            md = markdown.Markdown(extensions=self.extensions)
            html = md.convert(md_file.read())
            tmp_data = md.Meta
            self.console.log(md.Meta)
            # use uuid to solve the same name
            alt_path = uuid.uuid1().hex
            self.blog_tag_list += md.Meta["tags"]
            self.blog_categary_list += md.Meta["categories"]
            tmp_data["alt_path"] = alt_path
            tmp_data["toc"] = md.toc
            tmp_data["toc_tokens"] = md.toc_tokens
            if content:
                tmp_data["content"] = html
            data[alt_path] = tmp_data
            # self.console.log(md.toc_tokens)
        data = json.dumps(data, ensure_ascii=False)
        self.blog_all_list_data = data
        with open(json_file_path, "w", encoding="utf-8") as file:
            file.write(data)
        self.console.log(md_file_path + " -> md2json convert done")

    # TODO: 2021-01-27 Liona Maskros <lionacc@163.com> #
    def makeup_with_meta_info():
        """group the markdown info

        group markdown files with tags and categories

        """
        pass

    def run(self):
        self.make_blog_all_list()
        self.make_repos_list()
        self.make_about_page()


if __name__ == "__main__":
    store_path = "src/assets/data/"
    repos_api = "https://api.github.com/users/aislinge/repos"
    markdown_store_dir = r"./docs/"
    builder = Make_date(markdown_store_dir, store_path, repos_api)
    builder.run()
