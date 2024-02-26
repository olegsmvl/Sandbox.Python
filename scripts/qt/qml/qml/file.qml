import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12
import QtQuick.Layouts 1.12

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "XCP"

    GridLayout {
        id: gridLayout
        anchors.fill: parent
        columns: 2 // Количество столбцов в сетке
        rows: 6 // Количество строк в сетке

        Button {
            text: "Нажми меня"
            Layout.column: 0 // Размещаем во втором столбце
            Layout.row: 0
            onClicked: model.incrementCounter()
        }

        Text {
            text: "Секунды: " + model.secondsCounter
            Layout.column: 1 // Размещаем во втором столбце
            Layout.row: 0 // Размещаем в первой строке
            font.pixelSize: 24
        }

        TextInput {
            id: floatInput
            Layout.column: 0 // Размещаем во втором столбце
            Layout.row: 1
            font.pixelSize: 16
            inputMethodHints: Qt.ImhFormattedNumbersOnly | Qt.ImhAllowDecimal
            validator: DoubleValidator { bottom: -999999.0; top: 999999.0; decimals: 2 }
        }
        TextInput {
            id: integerInput
            Layout.column: 0 
            Layout.row: 2
            font.pixelSize: 16
            inputMethodHints: Qt.ImhDigitsOnly
            validator: IntValidator { bottom: -999999; top: 999999 }
        }
        TextField {
            placeholderText: "              "
            width: 250
            height: 40
            Layout.column: 1 
            Layout.row: 3
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

        Button {
            text: "Connect"
            Layout.column: 0 // Размещаем во втором столбце
            Layout.row: 3
            onClicked: model.connect()
        }
    }
}
