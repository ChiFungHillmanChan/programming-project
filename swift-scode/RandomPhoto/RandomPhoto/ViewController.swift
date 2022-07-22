//
//  ViewController.swift
//  RandomPhoto
//
//  Created by Hillman Chan on 10/07/2022.
//

import UIKit

class ViewController: UIViewController {
    
    private let imageView: UIImageView = {
        let imageView = UIImageView()
        imageView.contentMode = .scaleAspectFill
        imageView.backgroundColor = .white
        return imageView
    }()
    
    private let button: UIButton = {
        let button = UIButton()
        button.backgroundColor = .white
        button.setTitle("Random Photo", for: .normal)
        button.setTitleColor(.black, for: .normal)
        return button
    }()

    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        view.backgroundColor = .systemPink
        view.addSubview(imageView)
        imageView.frame = CGRect(x: 0, y: 0, width: 300, height: 300)
        imageView.center = view.center
        
        
        view.addSubview(button)
        button.frame = CGRect
        (x: 20, y: view.frame.size.height - 50 - view.safeAreaInsets.bottom, width: view.frame.size.width-40, height: 50)
        getRandomPhoto()
    }
    func getRandomPhoto() {
        let urlString = "https://source.unsplash.com/random/600x600"
        let url = URL(string: urlString)!
        guard let data = try? Data(contentsOf: url)else{
            return
        }
        imageView.image = UIImage(data: data)
    }


}

