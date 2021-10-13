from .telenium_process import TeleniumTestProcess
from .common import skip_screen_checks
from .common import ordered


test_address = {
    'recipient': 'BM-2cVpswZo8rWLXDVtZEUNcDQvnvHJ6TLRYr'
}


class MyAddressScreen(TeleniumTestProcess):
    """MyAddress Screen Functionality Testing"""
    subject = 'Hey this is Demo Subject'
    body = 'Hey,i am sending message directly from MyAddress book'

    @skip_screen_checks
    @ordered
    def test_select_myaddress_list(self):
        """Select Address From List of Address"""
        # This is for checking Current screen
        self.assert_wait_no_except('//ScreenManager[@current]', timeout=15, value='inbox')
        # This is for checking the Side nav Bar is closed
        self.open_side_navbar()
        # this is for scrolling Nav drawer
        self.drag("//NavigationItem[@text=\"Sent\"]", "//NavigationItem[@text=\"Inbox\"]")
        # assert for checking scroll function
        self.assertCheckScrollDown('//ContentNavigationDrawer//ScrollView[0]', timeout=3)
        # this is for opening My Address screen
        self.cli.wait_click('//NavigationItem[@text=\"My addresses\"]', timeout=2)
        # Checking current screen
        self.assertExists("//ScreenManager[@current=\"myaddress\"]", timeout=3)

    @skip_screen_checks
    @ordered
    def test_send_message_from(self):
        """Send Message From send Button"""
        # This is for checking Current screen
        self.assertExists("//ScreenManager[@current=\"myaddress\"]", timeout=3)
        # Click on Address to open popup
        self.cli.wait_click('//MDList[0]/CustomTwoLineAvatarIconListItem[0]', timeout=2)
        # Checking Popup Opened
        self.assertExists('//MyaddDetailPopup//MDLabel[@text=\"Send message from\"]', timeout=2)
        # Click on Send Message Button to redirect Create Screen
        self.cli.wait_click('//MyaddDetailPopup//MDRaisedButton[0]/MDLabel[@text=\"Send message from\"]', timeout=2)
        # Checking Current screen(Create)
        self.assertExists("//ScreenManager[@current=\"create\"]", timeout=2)
        # Entering Receiver Address
        self.cli.setattr(
            '//DropDownWidget/ScrollView[0]//MyTextInput[0]', "text", test_address['recipient'])
        # Checking Receiver Address filled or not
        self.assertExists('//DropDownWidget//MyTextInput[@text=\"{}\"]'.format(test_address['recipient']), timeout=5)
        # ADD SUBJECT
        self.cli.setattr('//DropDownWidget/ScrollView[0]//MyMDTextField[0]', 'text', self.subject)
        # Checking Subject Field is Entered
        self.assertExists(
            '//DropDownWidget/ScrollView[0]//MyMDTextField[@text=\"{}\"]'.format(self.subject), timeout=5)
        # ADD MESSAGE BODY
        self.cli.setattr(
            '//DropDownWidget/ScrollView[0]//ScrollView[0]/MDTextField[0]', 'text',
            self.body)
        # Checking Message body is Entered
        self.assertExists(
            '//DropDownWidget/ScrollView[0]//ScrollView[0]/MDTextField[@text=\"{}\"]'.format(self.body), timeout=5)
        # Click on BACK button
        self.cli.wait_click('//MDToolbar//MDActionTopAppBarButton[@icon=\"arrow-left\"]', timeout=2)
        # Check for redirected screen (Inbox Screen)
        self.assertExists("//ScreenManager[@current=\"inbox\"]", timeout=7)

    @skip_screen_checks
    @ordered
    def test_show_qrcode(self):
        """Show the Qr code of selected address"""
        # This is for checking the Side nav Bar is closed
        self.open_side_navbar()
        # Clicking on Sent Tab
        self.cli.wait_click('//NavigationItem[@text=\"My addresses\"]', timeout=3)
        # Checking current screen
        self.assertExists("//ScreenManager[@current=\"myaddress\"]", timeout=3)
        # Click on Address to open popup
        self.cli.wait_click('//MDList[0]/CustomTwoLineAvatarIconListItem[0]', timeout=2)
        # Check the Popup is opened
        self.assertExists('//MyaddDetailPopup//MDLabel[@text=\"Show QR code\"]', timeout=2)
        # Cick on 'Show QR code' button to view QR Code
        self.cli.wait_click('//MyaddDetailPopup//MDLabel[@text=\"Show QR code\"]')
        # Check Current screen is QR Code screen
        self.assertExists("//ScreenManager[@current=\"showqrcode\"]", timeout=2)
        # Click on BACK button
        self.cli.wait_click('//MDToolbar//MDActionTopAppBarButton[@icon=\"arrow-left\"]', timeout=2)
        # Checking current screen(My Address) after BACK press
        self.assertExists("//ScreenManager[@current=\"myaddress\"]", timeout=3)
