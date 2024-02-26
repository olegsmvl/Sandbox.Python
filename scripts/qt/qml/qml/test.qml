import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import QtQuick.Window 2.12

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "Передача числа из ввода в модель"

    // Модель
    Item {
        id: yourModel
        property int someProperty: 0 // Свойство для хранения числа
    }

    Label {
        text: "Введите целое число:"
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        font.pixelSize: 16
    }

    TextInput {
        id: integerInput
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        font.pixelSize: 16
        inputMethodHints: Qt.ImhDigitsOnly
        width: 200 // Ширина элемента TextInput
        height: 30 // Высота элемента TextInput
        anchors.fill: parent
        text: '234'

        onTextChanged: {
        // Передача значения в модель
        //yourModel.someProperty = parseInt(integerInput.text)
        }
    }

    TextField {
        placeholderText: "default TextField"
        width: 250
            height: 40
            background: Rectangle {
                border.color: "#C9C9C9"
                border.width: 1
            }
        inputMethodHints: Qt.ImhDigitsOnly
        //validator: IntValidator {bottom: 1; top: 100}
        validator : DoubleValidator {
        decimals: 2
        top: 99999
        bottom: -99999
        }
        onTextChanged: {
        // Передача значения в модель
        //yourModel.someProperty = parseInt(integerInput.text)
        }
    }

}