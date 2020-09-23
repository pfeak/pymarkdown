import os
from unittest import TestCase

from markdown import Markdown


class TestMarkdown(TestCase):

    def setUp(self) -> None:
        self.md = Markdown()

    def test_export(self):
        md = Markdown()
        md.add_h1("Title1")
        md.add_text("Content will not change to new line.", end=False)
        md.add_text("Content in the same line.")
        md.add_h2("Title2")
        md.add_strikethrough("Content deprecated", end=True)
        md.add_split_line()
        md.add_h2("Title3")
        md.add_quote("Quote content in this line.", end=False)
        md.add_bold("Bold Content", end=True)
        md.add_image(
            "https://timgsa.baidu.com/timg?image"
            "&quality=80&size=b9999_10000&sec=1600850864228"
            "&di=a9ef2aeb8fa4b61feb965a806cf3e69f"
            "&imgtype=0&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D159562664%2C875509196%26fm%3D214%26gp%3D0.jpg")
        md.add_image("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2931826153,3045777172&fm=26&gp=0.jpg",
                     alt="hello", title="image")
        md.export("test.md", path=os.getcwd())

        self.assertIsNotNone(self.md.get_content(), "content is null")
        print(f"{self.md.get_content()}")
        self.assertTrue(os.path.exists(self.md.get_export_path()), f"{self.md.get_export_path()} file is not exists !")
