import numpy as np
import matplotlib.pyplot as plt
import cv2

def hough(image, edge_image, num_rhos, num_thetas, bin_threshold):
  img_height, img_width = edge_image.shape[:2]
  img_height_half = img_height / 2
  img_width_half = img_width / 2
  
  diag_len = np.sqrt(img_height**2 + img_width**2)
  dtheta = 180 / num_thetas
  drho = (2 * diag_len) / num_rhos
  
  thetas = np.arange(0, 180, step=dtheta)
  
  rhos = np.arange(-diag_len, diag_len, step=drho)
  
  cos_thetas = np.cos(np.deg2rad(thetas))
  sin_thetas = np.sin(np.deg2rad(thetas))
  
  accumulator = np.zeros((len(rhos), len(thetas)))
  
  figure = plt.figure()
  hough_plot = figure.add_subplot()
  hough_plot.set_facecolor((0, 0, 0))
  hough_plot.title.set_text("Hough Space")
  
  for y in range(img_height):
    for x in range(img_width):
      if edge_image[y][x] != 0:
        edge_pt = [y - img_height_half, x - img_width_half]
        hough_rhos, hough_thetas = [], [] 
        
        for theta_idx in range(len(thetas)):
          rho = (edge_pt[1] * cos_thetas[theta_idx]) + (edge_pt[0] * sin_thetas[theta_idx])
          theta = thetas[theta_idx]
          
          rho_idx = np.argmin(np.abs(rhos - rho))
          
          accumulator[rho_idx][theta_idx] += 1
          
          hough_rhos.append(rho)
          hough_thetas.append(theta)
        
        hough_plot.plot(hough_thetas, hough_rhos, color="white", alpha=0.05)

  output_img = image.copy()
  out_lines = []
  
  for y in range(accumulator.shape[0]):
    for x in range(accumulator.shape[1]):
      if accumulator[y][x] > bin_threshold:
        rho = rhos[y]
        theta = thetas[x]
        
        a = np.cos(np.deg2rad(theta))
        b = np.sin(np.deg2rad(theta))
        
        x0 = (a * rho) + img_width_half
        y0 = (b * rho) + img_height_half
        
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        
        hough_plot.plot([theta], [rho], marker='o', color="#00FF00")
        
        output_img = cv2.line(output_img, (x1,y1), (x2,y2), (0,255,0), 1)
        
        out_lines.append((rho,theta,x1,y1,x2,y2))

  hough_plot.invert_yaxis()
  hough_plot.invert_xaxis()
  plt.show()
  
  return output_img, out_lines

