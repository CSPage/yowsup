from .message_media_downloadable import DownloadableMediaMessageProtocolEntity
from Yowsup.structs import ProtocolTreeNode
from Yowsup.structs.protocolentity import ProtocolEntityTest
from .test_message_media import MediaMessageProtocolEntityTest

class DownloadableMediaMessageProtocolEntityTest(MediaMessageProtocolEntityTest):
    def setUp(self):
        super(DownloadableMediaMessageProtocolEntityTest, self).setUp()
        self.ProtocolEntity = DownloadableMediaMessageProtocolEntity
        mediaNode = self.node.getChild("media")
        mediaNode.setAttribute("mimetype",  "MIMETYPE")
        mediaNode.setAttribute("filehash",  "FILEHASH")
        mediaNode.setAttribute("url",       "URL")
        mediaNode.setAttribute("ip",        "IP")
        mediaNode.setAttribute("size",      "SIZE")
        mediaNode.setAttribute("file",      "FILE")
